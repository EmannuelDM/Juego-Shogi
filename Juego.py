from Peon import Peon
from Alfil import Alfil
from Oro import Oro
from Plata import Plata
from Caballo import Caballo
from Torre import Torre
from Rey import Rey
from Lancero import Lancero

class Juego:
    def __init__(self):
        self.turno = 1
        self.board = []

        # Guardo a los reyes para consultar sus coordenadas en cada turno
        self.rey_player_1 = Rey(0, 4, 1, self.board)  # rey
        self.rey_player_2 = Rey(8, 4, 2, self.board)  # rey oponente

        # Inicializando Tablero
        self.board = [[0 for i in range(9)] for i in range(9)]
        for i in range(9):
            self.board[2][i] = Peon(2,i,1,self.board) # aqui van los peones
            self.board[6][i] = Peon(6,i,2,self.board) # aqui van los peones oponentes
        self.board[0][4] = self.rey_player_1
        self.board[8][4] = self.rey_player_2

        self.board[0][5] = Oro(0,5,1,self.board) # Oro derecho
        self.board[0][3] = Oro(0,3,1,self.board) # oro izquierdo

        self.board[8][5] = Oro(8,5,2,self.board) #oro der oponente
        self.board[8][3] = Oro(8,3,2,self.board) #oro izq oponente

        self.board[0][6] = Plata(0,6,1,self.board)  # Plata
        self.board[0][2] = Plata(0,2,1,self.board)  # Plata

        self.board[8][6] = Plata(8,6,2,self.board)  # Plata  oponente
        self.board[8][2] = Plata(8,2,2,self.board)  # Plata  oponente

        self.board[0][7] = Caballo(0,7,1,self.board)  # Caballo
        self.board[0][1] = Caballo(0,1,1,self.board)  # Caballo

        self.board[8][7] = Caballo(8,7,2,self.board)  # Caballo  oponente
        self.board[8][1] = Caballo(8,1,2,self.board)  # Caballo  oponente

        self.board[0][8] = Lancero(0,8,1,self.board)  # Lancero
        self.board[0][0] = Lancero(0,0,1,self.board)  # Lancero

        self.board[8][8] = Lancero(8,8,2,self.board)  # Lancero  oponente
        self.board[8][0] = Lancero(8,0,2,self.board)  # Lancero  oponente

        self.board[1][7] = Alfil(1,7,1,self.board)  # Alfil
        self.board[7][1] = Alfil(7,1,2,self.board)  # Alfil oponente

        self.board[1][1] = Torre(1,1,1,self.board)  # Torre
        self.board[7][7] = Torre(7,7,2,self.board)  # Torre oponente

    # Valida si el movimiento es posible
    def validar_movimiento(self, x,y, x2,y2):
        # Si no excede los limites horizontales
        if x2 < 9 and x2 >= 0:
            # Si no excede los limites verticales
            if y2 < 9 and y2 >= 0:
                # Si es una pieza(y no un espacio vacio) y es la pieza del jugador de turno
                if self.board[x][y] != 0 and self.board[x][y].jugador == self.turno:
                    # retornar True si el movimiento se puede hacer
                    return self.board[x][y].mover(x2,y2)
                else:
                    print("Pieza equivocada")
                    return False
            else:
                print("Movimiento fuera los limites")
                return False
        else:
            print("Movimiento fuera los limites")
            return False

    def mover_pieza(self, x,y, x2,y2):
        if(self.validar_movimiento( x,y, x2,y2)):
            # Hacer el traslado de la pieza a su nueva posicion
            self.board[x][y].x = x2
            self.board[x][y].y = y2
            self.board[x2][y2] = self.board[x][y]
            self.board[x][y] = 0
            self.cambiar_turno()
            return True
        else:
            return False

    def cambiar_turno(self):
        if self.turno == 1:
            self.turno = 2
        else:
            self.turno = 1
        self.es_jacke_mate()

    def promocionar_pieza(self, x, y):
        # Es una pieza promocionable?
        if hasattr(self.board[x][y], 'promocionada'):
            # Es una pieza del jugador de turno?
            if self.board[x][y].jugador == self.turno:
                # Es jugador Uno?
                if self.board[x][y].jugador == 1:
                    # Esta en el area de promocion?
                    if x > 5:
                        self.board[x][y].promocionar(True)
                        return True
                    else:
                        print("No esta en el area de promocion")
                        return False
                # Es jugador Dos
                else:
                    # Esta en el area de promocion?
                    if x < 3:
                        self.board[x][y].promocionar(True)
                        return True
                    else:
                        print("No esta en el area de promocion")
                        return False
            else:
                print("Elige una pieza tuya")
                return False
        else:
            print("No es promocionable")
            return False

    def recuperar_pieza(self):
        pass

    def es_jacke_mate(self):
        mov_del_rey = [] # Las diferentes coordenadas a las que puede moverse el rey
        piezas_flanqueantes = [] # lista de piezas que ponen en jaque al rey o que flanquean sus movimientos
        rey_en_jaque = False
        bloqueado = False # el rey esta bloqueado para hacer cualquier movimiento

        # Comprobar turno del jugador
        if self.turno == 1:
            rey = self.rey_player_1
        else:
            rey = self.rey_player_2

        #TODO contemplar que el rey no controla si hay piezas suyas alrededor
        # Guarda en la lista los movimientos que puede hacer actualmente el rey
        for mov in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]:
            if rey.mover(rey.x+mov[0], rey.y+mov[1]):
                mov_del_rey.append((rey.x+mov[0],rey.y+mov[1]))
        # Copia temporal de los mocimientos
        mov_del_rey_2 = mov_del_rey[:]
        #Recorro el tablero
        for fila in self.board:
            for pieza in fila:
                # Busco las piezas oponentes
                if pieza != 0 and pieza.jugador != self.turno:
                    # busco las piezas que puedan ponerlo en jaque
                    if pieza.mover(rey.x,rey.y):
                        rey_en_jaque = True
                        #TODO contemplar que no tengo que agregar mas de una vez la misma pieza
                        #TODO no se contempla que las piezas pueden considerar pasos fuera el tablero
                        piezas_flanqueantes.append(pieza)
                    # busco las piezas oponentes que bloqueen los movimientos del rey
                    for i in range(len(mov_del_rey)):
                        if pieza.mover(mov_del_rey[i][0],mov_del_rey[i][1]):
                            piezas_flanqueantes.append(pieza)
                            # Elimino de la segunda lista, esa coordenada flanqueda
                            for j in mov_del_rey_2:
                                if j[0] == mov_del_rey[i][0] and j[1] == mov_del_rey[i][1]:
                                    del mov_del_rey_2[mov_del_rey_2.index(j)]
        # Si todos los movimientos del rey estan bloqueados:
        if len(mov_del_rey_2) == 0:
            bloqueado = True
            print("Rey "+str(rey.jugador)+" bloqueado")
        if rey_en_jaque:
            print("Rey "+str(rey.jugador)+" en jaque")

        #TODO completar el resto del codigo para determinar si es mate

