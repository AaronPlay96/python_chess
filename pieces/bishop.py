from pieces import piece


class Bishop(piece.Piece):
    def __init__(self, px, py, color):
        if color:
            col = "white"
        else:
            col = "black"
        super().__init__(px, py, color)

    def move(self, x, y):
        self.pos_x = x
        self.pos_y = y
