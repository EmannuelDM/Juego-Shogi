
class PiezaShogi:
    def __init__(self,x,y,jugador, tablero):
        self.x = x
        self.y = y
        self.jugador = jugador
        self.tablero = tablero
        if jugador == 1:
            self.direccion = 1
        else:
            self.direccion = -1