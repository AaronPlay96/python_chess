from pieces import piece


class Bishop(piece.Piece):
    def __init__(self, px, py, color):
        super().__init__(px, py, color)

    def valid_moves(self, board):
        moves = []
        for i in range(7):
            if self.pos_x + 1 + i <= 7 and self.pos_y + 1 + i <= 7:
                if board[self.pos_x + 1 + i][self.pos_y + 1 + i] != 'e':
                    if board[self.pos_x + 1 + i][self.pos_y + 1 + i].white != self.white:
                        moves.append([self.pos_x + 1 + i, self.pos_y + 1 + i])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x + 1 + i, self.pos_y + 1 + i])

        for i in range(7):
            if self.pos_x - 1 - i >= 0 and self.pos_y - 1 - i >= 0:
                if board[self.pos_x - 1 - i][self.pos_y - 1 - i] != 'e':
                    if board[self.pos_x - 1 - i][self.pos_y - 1 - i].white != self.white:
                        moves.append([self.pos_x - 1 - i, self.pos_y - 1 - i])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x - 1 - i, self.pos_y - 1 - i])

        for i in range(7):
            if self.pos_x + 1 + i <= 7 and self.pos_y - 1 - i >= 0:
                if board[self.pos_x + 1 + i][self.pos_y - 1 - i] != 'e':
                    if board[self.pos_x + 1 + i][self.pos_y - 1 - i].white != self.white:
                        moves.append([self.pos_x + 1 + i, self.pos_y - 1 - i])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x + 1 + i, self.pos_y - 1 - i])

        for i in range(7):
            if self.pos_x - 1 - i >= 0 and self.pos_y + 1 + i <= 7:
                if board[self.pos_x - 1 - i][self.pos_y + 1 + i] != 'e':
                    if board[self.pos_x - 1 - i][self.pos_y + 1 + i].white != self.white:
                        moves.append([self.pos_x - 1 - i, self.pos_y + 1 + i])
                        break
                    else:
                        break
                else:
                    moves.append([self.pos_x - 1 - i, self.pos_y + 1 + i])
        return moves