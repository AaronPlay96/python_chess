from pieces import piece


class Rook(piece.Piece):
    def __init__(self, px, py, color):
        super().__init__( px, py, color)

    def valid_moves(self, board):
        moves = []
        for i in range(7):
            if self.pos_x + 1 + i <= 7:
                if board[self.pos_x + 1 + i][self.pos_y] != 'e':
                    if board[self.pos_x + 1 + i][self.pos_y].white != self.white:
                        moves.append([self.pos_x + 1 + i, self.pos_y])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x + 1 + i, self.pos_y])

        for i in range(7):
            if self.pos_x - 1 - i >= 0:
                if board[self.pos_x - 1 - i][self.pos_y] != 'e':
                    if board[self.pos_x - 1 - i][self.pos_y].white != self.white:
                        moves.append([self.pos_x - 1 - i, self.pos_y])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x - 1 - i, self.pos_y])

        for i in range(7):
            if self.pos_y + 1 + i <= 7:
                if board[self.pos_x][self.pos_y + 1 + i] != 'e':
                    if board[self.pos_x][self.pos_y  + 1 + i].white != self.white:
                        moves.append([self.pos_x, self.pos_y  + 1 + i])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x, self.pos_y + 1 + i])

        for i in range(7):
            if self.pos_y - 1 - i >= 0:
                if board[self.pos_x][self.pos_y - 1 - i] != 'e':
                    if board[self.pos_x][self.pos_y - 1 - i].white != self.white:
                        moves.append([self.pos_x, self.pos_y - 1 - i])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x, self.pos_y - 1 - i])
        return moves
