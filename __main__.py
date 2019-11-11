from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import tkinter as tk
from Juego import Juego


class Partida():
    def __init__(self):
        self.pieza_seleccionada = ()

        self.juego = Juego()
        self.raiz = Tk()
        self.raiz.geometry('700x500')
        self.raiz.configure(bg = 'beige')
        self.raiz.title('Shogi Time')
        ttk.Button(self.raiz, text='Salir',
                   command=self.raiz.destroy)

        self.graphicBoard = self.get_board()

        self.PromButton = tk.Button(self.raiz, text = "Promocionar")
        self.PromButton.config(command = self.promover)
        self.PromButton.grid(column=9, row=9)

        self.raiz.mainloop()


    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                b = tk.Button(self.raiz, text=self.get_name(i,j), height = 2, width = 5)
                b.config(command=lambda widget=b: self.click_button(widget))
                b.grid(column=j, row=i)
                #Store row and column indices as a Button attribute
                b.position = (i, j)
                row.append(b)
            board.append(row)
        return board

    def get_name(self,i,j):
        if self.juego.board[i][j] != 0:
            return self.juego.board[i][j].nombre
        else:
            return " "

    def click_button(self, widget):
        print(widget.position)
        x,y = widget.position
        widget.focus()
        # Se hizo click en una pieza de shogi?
        if self.juego.board[x][y] != 0:
            # Es una pieza del jugador de turno?
            if self.juego.board[x][y].jugador == self.juego.turno:
                self.pieza_seleccionada = (x,y)
            # Sino, es una pieza del otro jugador
            else:
                # si se selecciono una pieza propia previamente, estaran guardadas sus coordenadas como una tupla
                if len(self.pieza_seleccionada) != 0:
                    # Movimiento de pieza exitoso?
                    if self.juego.mover_pieza(self.pieza_seleccionada[0],self.pieza_seleccionada[1],x,y):
                        widget.configure(text = self.get_name(x,y))
                        self.graphicBoard[self.pieza_seleccionada[0]][self.pieza_seleccionada[1]].configure(text=" ")
                        self.PromButton.config(state=NORMAL) # habilitar boton de promocion
                        self.pieza_seleccionada = ()

                else:
                    print("Seleccione una pieza suya")
        # Se hizo click en un espacio vacio
        else:
            # si se selecciono una pieza propia previamente, estaran guardadas sus coordenadas como una tupla
            if len(self.pieza_seleccionada) != 0:
                # Movimiento de pieza exitoso?
                if self.juego.mover_pieza(self.pieza_seleccionada[0], self.pieza_seleccionada[1], x, y):
                    widget.configure(text=self.get_name(x, y))
                    self.graphicBoard[self.pieza_seleccionada[0]][self.pieza_seleccionada[1]].configure(text=" ")
                    self.PromButton.config(state = NORMAL) # habilitar boton de promocion
                    self.pieza_seleccionada = ()
            else:
                print("Falta seleccionar una pieza")

    def promover(self):
        # pieza seleccionada previamente?
        if len(self.pieza_seleccionada) != 0:
            x = self.pieza_seleccionada[0]
            y = self.pieza_seleccionada[1]
            if(self.juego.promocionar_pieza(x,y)):
                print("Pieza promocionada")
                self.PromButton.config(state = DISABLED) # Deshabilitar boton de promocion
                self.graphicBoard[x][y].config(text = self.get_name(x,y))
        else:
            print("Seleccione una pieza")


def main():
    NuevaPartida = Partida()
    return 0

if __name__ == '__main__':
    main()