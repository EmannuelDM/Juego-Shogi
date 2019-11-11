from PiezaShogi import PiezaShogi
from MovDiagonal import MovDiagonal
from MovCruz import  MovCruz

class Plata(PiezaShogi,MovDiagonal,MovCruz):
    def __init__(self,x,y,jugador, tablero):
        PiezaShogi.__init__(self,x,y,jugador, tablero)
        self.promocionada = False
        self.nombre = str(self.jugador) + "Pl"

    def mover(self, x2, y2):
        diferenciax = x2-self.x
        diferenciay = y2-self.y
        if self.promocionada:
            if self.un_paso_en_cruz(x2, y2):
                return True
            else:
                if abs(y2 - self.y) == (x2 - self.x) * self.direccion == 1:
                    return True
                else:
                    return False
        else:
            if self.un_paso_diagonal(diferenciax, diferenciay):
                return True
            else:
                if diferenciay == 0 and diferenciax*self.direccion == 1:
                    return True
                else:
                    return False

    def promocionar(self, booleano):
        if booleano:
            self.promocionada = True
            self.nombre = str(self.jugador)+"Pl+"
        else:
            self.promocionada = False
            self.nombre = str(self.jugador) + "Pl"
