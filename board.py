"""
   notation for bidimensional array that contains the details about the pieces in the chess board
   e - empty
   p/P - Pawn
   r/R - Rook
   b/B - Bishop
   n/N - Knight
   q/Q - Queen
   k/K - King

   lowercase stand for the white pieces and uppercase for the black ones.
"""
from pieces import *

class Board:
    def __init__(self):
        self.board = [['e'] * 8] * 8
        self.board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        self.board[1] = ['p'] * 8
        self.board[6] = ['P'] * 8
        self.board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

        self.pieces = [['e'] * 8] * 8
        self.pieces[0] = [Rook(0, 0, True), Knight(0, 1, True), Bishop(0, 2, True), Queen(0, 3, True),
                         King(0, 4, True), Bishop(0, 5, True), Knight(0, 6, True), Rook(0, 7, True)]
        self.pieces[1] = [Pawn(1, 0, True), Pawn(1, 1, True), Pawn(1, 2, True), Pawn(1, 3, True),
                         Pawn(1, 4, True), Pawn(1, 5, True), Pawn(1, 6, True), Pawn(1, 7, True)]
        self.pieces[6] = [Pawn(6, 0, False), Pawn(6, 1, False), Pawn(6, 2, False), Pawn(6, 3, False),
                         Pawn(6, 4, False), Pawn(6, 5, False), Pawn(6, 6, False), Pawn(6, 7, False)]
        self.pieces[7] = [Rook(7, 0, False), Knight(7, 1, False), Bishop(7, 2, False), Queen(7, 3, False),
                         King(7, 4, False), Bishop(7, 5, False), Knight(7, 6, False), Rook(7, 7, False)]

    def get_board(self):
        return self.board

    def set_board(self, b):
        self.board = b
