from pieces import piece


class King(piece.Piece):
    def __init__(self, px, py, color):
        super().__init__(px, py, color)

    def valid_moves(self, board):
        moves = []

        if self.pos_x + 1 <= 7:
            if board[self.pos_x + 1][self.pos_y] != 'e':
                if board[self.pos_x + 1][self.pos_y].white != self.white:
                    moves.append([self.pos_x + 1, self.pos_y])
            else:
                moves.append([self.pos_x + 1, self.pos_y])

        if self.pos_x - 1 >= 0:
            if board[self.pos_x - 1][self.pos_y] != 'e':
                if board[self.pos_x - 1][self.pos_y].white != self.white:
                    moves.append([self.pos_x - 1, self.pos_y])
            else:
                moves.append([self.pos_x - 1, self.pos_y])

        if self.pos_y + 1 <= 7:
            if board[self.pos_x][self.pos_y + 1] != 'e':
                if board[self.pos_x][self.pos_y + 1].white != self.white:
                    moves.append([self.pos_x, self.pos_y + 1])
            else:
                moves.append([self.pos_x, self.pos_y + 1])

        if self.pos_y - 1 >= 0:
            if board[self.pos_x][self.pos_y - 1] != 'e':
                if board[self.pos_x][self.pos_y - 1].white != self.white:
                    moves.append([self.pos_x, self.pos_y - 1])
            else:
                moves.append([self.pos_x, self.pos_y - 1])

        if self.pos_x + 1 <= 7 and self.pos_y + 1 <= 7:
            if board[self.pos_x + 1][self.pos_y + 1] != 'e':
                if board[self.pos_x + 1][self.pos_y + 1].white != self.white:
                    moves.append([self.pos_x + 1, self.pos_y + 1])
            else:
                moves.append([self.pos_x + 1, self.pos_y + 1])

        if self.pos_x + 1 <= 7 and self.pos_y - 1 >= 0:
            if board[self.pos_x + 1][self.pos_y - 1] != 'e':
                if board[self.pos_x + 1][self.pos_y - 1].white != self.white:
                    moves.append([self.pos_x + 1, self.pos_y - 1])
            else:
                moves.append([self.pos_x + 1, self.pos_y - 1])

        if self.pos_x - 1 >= 0 and self.pos_y + 1 <= 7:
            if board[self.pos_x - 1][self.pos_y + 1] != 'e':
                if board[self.pos_x - 1][self.pos_y + 1].white != self.white:
                    moves.append([self.pos_x - 1, self.pos_y + 1])
            else:
                moves.append([self.pos_x - 1, self.pos_y + 1])

        if self.pos_x - 1 >= 0 and self.pos_y + 1 >= 0:
            if board[self.pos_x - 1][self.pos_y - 1] != 'e':
                if board[self.pos_x - 1][self.pos_y - 1].white != self.white:
                    moves.append([self.pos_x - 1, self.pos_y - 1])
            else:
                moves.append([self.pos_x - 1, self.pos_y - 1])

        return moves