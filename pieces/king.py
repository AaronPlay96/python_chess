from pieces import piece


class King(piece.Piece):
    def __init__(self, px, py, color):
        if color:
            col = "white"
        else:
            col = "black"
        super().__init__(px, py, color)