from PiezaShogi import PiezaShogi

class Rey(PiezaShogi):
    def __init__(self,x,y,jugador, tablero):
        PiezaShogi.__init__(self,x,y,jugador, tablero)
        self.nombre = str(self.jugador) + "R"


    def mover(self, x2, y2):
        if abs(x2-self.x) < 2 and abs(y2-self.y) <2:
            return True
        else:
            return False