from pieces import piece


class Pawn(piece.Piece):
    def __init__(self, px, py, color):
        is_pawn = True
        super().__init__(px, py, color)

    def valid_moves(self, board):
        moves = []
        if self.white:
            if board[self.pos_x + 1][self.pos_y] == 'e':
                moves.append([self.pos_x + 1, self.pos_y])
            if self.pos_y <= 6:
                if board[self.pos_x + 1][self.pos_y + 1] != 'e' and not board[self.pos_x + 1][self.pos_y + 1].white:
                    moves.append([self.pos_x + 1, self.pos_y + 1])
            if self.pos_y >= 1:
                if board[self.pos_x + 1][self.pos_y - 1] != 'e' and not board[self.pos_x + 1][self.pos_y - 1].white:
                    moves.append([self.pos_x + 1, self.pos_y - 1])
            if not self.moved and board[self.pos_x + 2][self.pos_y] == 'e':
                moves.append([self.pos_x + 2, self.pos_y])
        else:
            if board[self.pos_x - 1][self.pos_y] == 'e':
                moves.append([self.pos_x - 1, self.pos_y])
            if self.pos_y <= 6:
                if board[self.pos_x - 1][self.pos_y + 1] != 'e' and board[self.pos_x - 1][self.pos_y + 1].white:
                    moves.append([self.pos_x - 1, self.pos_y + 1])
            if self.pos_y >= 1:
                if board[self.pos_x - 1][self.pos_y - 1] != 'e' and board[self.pos_x - 1][self.pos_y - 1].white:
                    moves.append([self.pos_x - 1, self.pos_y - 1])
            if not self.moved and board[self.pos_x - 2][self.pos_y] == 'e':
                moves.append([self.pos_x - 2, self.pos_y])
        return moves
