from PiezaShogi import PiezaShogi
from MovCruz import MovCruz

class Caballo(PiezaShogi, MovCruz):
    def __init__(self,x,y,jugador, tablero):
        PiezaShogi.__init__(self,x,y,jugador, tablero)
        self.promocionada = False
        self.nombre = str(self.jugador) + "C"

    def mover(self, x2, y2):
        if self.promocionada:
            if self.un_paso_en_cruz(x2, y2):
                return True
            else:
                if abs(y2 - self.y) == (x2 - self.x) * self.direccion == 1:
                    return True
                else:
                    return False
        else:
            if abs(y2-self.y) == 1 and (x2-self.x)*self.direccion == 2:
                return True
            else:
                return False

    def promocionar(self, booleano):
        if booleano:
            self.promocionada = True
            self.nombre = str(self.jugador)+"C+"
        else:
            self.promocionada = False
            self.nombre = str(self.jugador) + "C"