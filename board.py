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
        # array for UI display
        self.board = [['.'] * 8] * 8
        self.board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        self.board[1] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
        self.board[2] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.board[3] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.board[4] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.board[5] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.board[6] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
        self.board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

        # pieces array for state control
        self.pieces = [['.'] * 8] * 8
        self.pieces[0] = [Rook(0, 0, True), Knight(0, 1, True), Bishop(0, 2, True), Queen(0, 3, True),
                          King(0, 4, True), Bishop(0, 5, True), Knight(0, 6, True), Rook(0, 7, True)]
        self.pieces[1] = [Pawn(1, 0, True), Pawn(1, 1, True), Pawn(1, 2, True), Pawn(1, 3, True),
                          Pawn(1, 4, True), Pawn(1, 5, True), Pawn(1, 6, True), Pawn(1, 7, True)]
        self.pieces[2] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.pieces[3] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.pieces[4] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.pieces[5] = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
        self.pieces[6] = [Pawn(6, 0, False), Pawn(6, 1, False), Pawn(6, 2, False), Pawn(6, 3, False),
                          Pawn(6, 4, False), Pawn(6, 5, False), Pawn(6, 6, False), Pawn(6, 7, False)]
        self.pieces[7] = [Rook(7, 0, False), Knight(7, 1, False), Bishop(7, 2, False), Queen(7, 3, False),
                          King(7, 4, False), Bishop(7, 5, False), Knight(7, 6, False), Rook(7, 7, False)]

    def move(self, i, j, x, y):
        if [x, y] in self.pieces[i][j].valid_moves(self.pieces):
            # moving the piece in the board array
            self.board[x][y] = self.board[i][j]
            self.board[i][j] = 'e'
            # moving the piece in the piece array
            self.pieces[x][y] = self.pieces[i][j]
            self.pieces[i][j] = 'e'
            self.pieces[x][y].pos_x = x
            self.pieces[x][y].pos_y = y
            self.pieces[x][y].moved = True
            self.pieces[x][y].selected = False
            return True
        else:
            self.pieces[i][j].selected = False
            return False
