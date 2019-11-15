# Testeando una situacion de jacke mate
#
# self.rey_player_1 = Rey(8, 4, 1, self.board)  # rey
# self.rey_player_2 = Rey(5, 5, 2, self.board)  # rey oponente
#
# # Inicializando Tablero
# self.board = [[0 for i in range(9)] for i in range(9)]
# self.board[8][4] = self.rey_player_1
# self.board[5][5] = self.rey_player_2
#
# self.board[4][5] = Oro(4, 5, 1, self.board)  # oro der oponente
#
# self.board[2][3] = Alfil(2, 3, 2, self.board)  # Alfil
# self.board[3][6] = Alfil(3, 6, 1, self.board)  # Alfil oponente
#
# self.board[6][7] = Torre(6, 7, 1, self.board)  # Torre oponente



# Los movimientos de cada pieza fueron testeados manualmente durante una partida, moviendo
# cada pieza a todas las posiciones posibles adyacentes, permitidas y no permitidas
# Igualmente para las promociones y sus movimientos
# Preferi hacerlo de esta forma por que es una manera visual e interactiva de testear el juego,
# a su vez,es mas rapida que escribir los test unitarios para cada uno de los movimientos de cada una de las piezas
# Ademas implicaria armar el entorno apropiado en el tablero, lo cual por motivos de mi diseño,
# no puede aislarse y pasarse como parametro en una  funcion que testea unitariamente.




