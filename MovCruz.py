class MovCruz:

    # Devuelve verdadero si se puede llevar a cabo un paso en cruz, sino, devuelve falso
    def un_paso_en_cruz(self, x2, y2):
        # Es un paso vertical?
        if abs(x2 - self.x) == 1 and abs(y2 - self.y) == 0:
            return True
        # Es un paso horizontal?
        elif abs(y2 - self.y) == 1 and abs(x2 - self.x) == 0:
            return True
        else:
            return False

    # True si se puede realizar un mov vertical
    def mov_vertical(self,x2,y2):
        if abs(x2-self.x)!=0 and abs(y2-self.y)==0:
            # verifico que en el trayecto no haya una pieza que obstaculice el camino
            for i in range(min(self.x, x2)+1,max(self.x, x2)):
                if self.tablero[i][y2] != 0:
                    return False
            return True
        else:
            return False

    # True si se puede realizar un mov Horizontal
    def mov_horizontal(self,x2,y2):
        if (abs(y2-self.y) !=0 ) and (abs(x2-self.x) == 0):
            # verifico que en el trayecto no haya una pieza que obstaculice el camino
            for i in range(min(self.y, y2)+1,max(self.y, y2)):
                if self.tablero[x2][i] != 0:
                    return False
            return True
        else:
            return False