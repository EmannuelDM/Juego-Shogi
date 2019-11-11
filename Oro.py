from PiezaShogi import PiezaShogi
from MovDiagonal import MovDiagonal
from MovCruz import MovCruz


class Oro(PiezaShogi,MovDiagonal,MovCruz):
    def __init__(self,x,y,jugador, tablero):
        PiezaShogi.__init__(self,x,y,jugador, tablero)
        self.nombre = str(self.jugador) + "O"

    def mover(self, x2, y2):
        if self.un_paso_en_cruz(x2,y2):
            return True
        else:
            if abs(y2-self.y) == (x2-self.x)*self.direccion == 1 :
                return True
            else:
                return False

