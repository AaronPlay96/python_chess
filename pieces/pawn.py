from pieces import piece


class Pawn(piece.Piece):
    def __init__(self, px, py, color):
        super().__init__(px, py, color)

    def valid_moves(self):
        return [[self.pos_x + 1, self.pos_y]]
