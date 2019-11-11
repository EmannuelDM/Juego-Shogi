from MovDiagonal import MovDiagonal
from MovCruz import MovCruz
from PiezaShogi import PiezaShogi

class Alfil(PiezaShogi, MovDiagonal, MovCruz):
    def __init__(self,x,y,jugador, tablero):
        PiezaShogi.__init__(self,x,y,jugador, tablero)
        self.promocionada = False
        self.nombre = str(self.jugador)+"A"

    def mover(self, x2, y2):
        diferenciax = x2 - self.x
        diferenciay = y2 - self.y
        # Si el Movimiento es diagonal y diferente de la posicion actual
        if self.es_mov_diagonal(diferenciax,diferenciay):
            return self.movimiento_diagonal(diferenciax,diferenciay)
        # Sino, si esta promocionado, intentar un paso en cruz
        elif self.promocionada:
            return self.un_paso_en_cruz(x2,y2)
        else:
            # Si no esta promocionado
            return False

    def promocionar(self, booleano):
        if booleano:
            self.promocionada = True
            self.nombre = str(self.jugador)+"A+"
        else:
            self.promocionada = False
            self.nombre = str(self.jugador) + "A"