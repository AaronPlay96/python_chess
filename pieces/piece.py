class Piece:
    """
    Sprite_path = ""  # url for the actual piece sprite
    pos_x = 0  # x coordinate for the position of the piece
    pos_y = 0  # x coordinate for the position of the piece
    white = True  # flag that indicates if the piece is white or not
    alive = True  # flag that indicates if the piece is in the board or not
    """

    def __init__(self, px, py, color):
        self.pos_x = px
        self.pos_y = py
        self.white = color
        self.moved = False
        self.selected = False
        self.is_pawn = False

    # movement method, this method will be overitten in each one of the pieces for its particular behaviour.
    def valid_moves(self, board):
        pass
