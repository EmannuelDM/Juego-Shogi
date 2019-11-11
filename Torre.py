from MovCruz import MovCruz
from MovDiagonal import MovDiagonal
from PiezaShogi import PiezaShogi

class Torre(PiezaShogi,MovCruz,MovDiagonal):
    def __init__(self,x,y,jugador, tablero):
        PiezaShogi.__init__(self,x,y,jugador, tablero)
        self.promocionada = False
        self.nombre = str(self.jugador) + "T"

    def mover(self, x2, y2):

        # Movimiento vertical
        if self.mov_vertical(x2,y2):
            return True
        # Movimiento horizontal
        elif self.mov_horizontal(x2,y2):
            return True
        elif self.promocionada:
            # Si el movimiento en diagonal es solo de un paso
            diferenciax = self.x-x2
            diferenciay = self.y-y2
            return self.un_paso_diagonal(diferenciax,diferenciay)
        else:
            return False

    def promocionar(self, booleano):
        if booleano:
            self.promocionada = True
            self.nombre = str(self.jugador)+"T+"
        else:
            self.promocionada = False
            self.nombre = str(self.jugador) + "T"