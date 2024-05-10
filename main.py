import sys
from board import *
from art import *

NOMBRE_JUEGO=text2art("Conecta 4 CLI")






if __name__ == '__main__':
    print(NOMBRE_JUEGO)
    board = Board()

    board.print_board()
    board.update_board(1,1)
    board.update_board(1,1)
    board.update_board(1,1)
    board.print_board()

