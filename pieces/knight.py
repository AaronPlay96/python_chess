from pieces import piece


class Knight(piece.Piece):
    def __init__(self, px, py, color):
        super().__init__(px, py, color)

    def valid_moves(self, board):
        moves = []

        if self.pos_x + 2 <= 7 and self.pos_y - 1 >= 0:
            if board[self.pos_x + 2][self.pos_y - 1] != 'e':
                if board[self.pos_x + 2][self.pos_y - 1].white != self.white:
                    moves.append([self.pos_x + 2, self.pos_y - 1])
            else:
                moves.append([self.pos_x + 2, self.pos_y - 1])
        if self.pos_x + 2 <= 7 and self.pos_y + 1 <= 7:
            if board[self.pos_x + 2][self.pos_y + 1] != 'e':
                if board[self.pos_x + 2][self.pos_y + 1].white != self.white:
                    moves.append([self.pos_x + 2, self.pos_y + 1])
            else:
                moves.append([self.pos_x + 2, self.pos_y + 1])
        if self.pos_x - 2 >= 0 and self.pos_y - 1 >= 0:
            if board[self.pos_x - 2][self.pos_y - 1] != 'e':
                if board[self.pos_x - 2][self.pos_y - 1].white != self.white:
                    moves.append([self.pos_x - 2, self.pos_y - 1])
            else:
                moves.append([self.pos_x - 2, self.pos_y - 1])
        if self.pos_x - 2 >= 1 and self.pos_y + 1 <= 7:
            if board[self.pos_x - 2][self.pos_y + 1] != 'e':
                if board[self.pos_x - 2][self.pos_y + 1].white != self.white:
                    moves.append([self.pos_x - 2, self.pos_y + 1])
            else:
                moves.append([self.pos_x - 2, self.pos_y + 1])
        if self.pos_x + 1 <= 7 and self.pos_y - 2 >= 0:
            if board[self.pos_x + 1][self.pos_y - 2] != 'e':
                if board[self.pos_x + 1][self.pos_y - 2].white != self.white:
                    moves.append([self.pos_x + 1, self.pos_y - 2])
            else:
                moves.append([self.pos_x + 1, self.pos_y - 2])
        if self.pos_x + 1 <= 7 and self.pos_y + 2 <= 7:
            if board[self.pos_x + 1][self.pos_y + 2] != 'e':
                if board[self.pos_x + 1][self.pos_y + 2].white != self.white:
                    moves.append([self.pos_x + 1, self.pos_y + 2])
            else:
                moves.append([self.pos_x + 1, self.pos_y - 2])
        if self.pos_x - 1 >= 0 and self.pos_y + 2 <= 7:
            if board[self.pos_x - 1][self.pos_y + 2] != 'e':
                if board[self.pos_x - 1][self.pos_y + 2].white != self.white:
                    moves.append([self.pos_x - 1, self.pos_y + 2])
            else:
                moves.append([self.pos_x - 1, self.pos_y + 2])
        if self.pos_x - 1 >= 0 and self.pos_y - 2 >= 0:
            if board[self.pos_x - 1][self.pos_y - 2] != 'e':
                if board[self.pos_x - 1][self.pos_y - 2].white != self.white:
                    moves.append([self.pos_x - 1, self.pos_y - 2])
            else:
                moves.append([self.pos_x - 1, self.pos_y - 2])
        return moves
