
class MovDiagonal:

    # Devuelve verdadero si es movimiento diagonal o falso si no lo es
    def es_mov_diagonal(self, diferenciax, diferenciay):
        if abs(diferenciax) == abs(diferenciay) != 0:
            return True
        else:
            return False

    # Devuelve verdadero si se puede ejecutar el movimiento diagonal o Falso si encontro un obstaculo en el camino
    def movimiento_diagonal(self, diferenciax, diferenciay):
        # verifico que en el trayecto no haya una pieza que obstaculice el camino
        # Si tienen el mismo signo, describen una pendiente positiva
        if diferenciax == diferenciay:
            if diferenciax > 0:
                for i in range(1, abs(diferenciax)):
                    if (self.tablero[self.x + i][self.y + i] != 0):
                        return False
            if diferenciax < 0:
                for i in range(1, abs(diferenciax)):
                    if (self.tablero[self.x - i][self.y - i] != 0):
                        return False
            return True
        # Sino, describe una pendiente negativa
        else:
            if diferenciax > 0:
                for i in range(1, abs(diferenciax)):
                    if (self.tablero[self.x + i][self.y - i] != 0):
                        return False
            if diferenciax < 0:
                for i in range(1, abs(diferenciax)):
                    if (self.tablero[self.x - i][self.y + i] != 0):
                        return False
            return True
        # Otra forma de hacerlo
        # if diferenciax == diferenciay:
        #     for i in range(min(self.x,x2)+1,max(self.x,x2)): # si no sumo 1, se detectaria a si mismo como obstaculo
        #         j = (i-self.x)+self.y # Ecuacion de punto - pendiente
        #         if(self.board[i][j] != 0):
        #             return False
        # else:
        #     for i in range(min(self.x,x2)+1,max(self.x,x2)): # si no sumo 1, se detectaria a si mismo como obstaculo
        #         j = -1*(i-self.x)+self.y # Ecuacion de punto - pendiente
        #         if(self.board[i][j] != 0):
        #             return False


    # Devuelve verdadero si es un paso diagonal o falso si no lo es
    def un_paso_diagonal(self, diferenciax, diferenciay):
        if abs(diferenciax)==abs(diferenciay)== 1:
            return True
        else:
            return False