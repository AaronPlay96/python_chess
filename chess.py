import arcade
from board import Board

TOTAL_SIZE = 600  # the size of the chess table with the image borders, the black lineas around the image.
TABLE_SIZE = 600  # the size of the chess table without the image borders.
SCREEN_TITLE = 'CHESS'
SPRITE_MAP = {'p': 'whitePawn', 'r': 'whiteRook', 'n': 'whiteKnight',
              'b': 'whiteBishop', 'q': 'whiteQueen', 'k': 'whiteKing',
              'P': 'blackPawn', 'R': 'blackRook', 'N': 'blackKnight',
              'B': 'blackBishop', 'Q': 'blackQueen', 'K': 'blackKing'}
board = Board()


def calculate_coordinates(sx, sy):
    return [((sx * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)), ((sy * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16))]


class MyGame(arcade.Window):
    global board
    global TOTAL_SIZE

    def __init__(self):
        super().__init__(TOTAL_SIZE + 200, TOTAL_SIZE, SCREEN_TITLE)
        self.set_mouse_visible(True)
        self.sx = 50  # coordinate x for selected piece outline
        self.sy = 50  # coordinate y for selected piece outline
        self.px = 0  # selected piece row values for piece array
        self.py = 0  # selected piece column values for piece array
        self.selection = False
        self.pos_mov = []
        self.turn = True

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(TOTAL_SIZE // 2, TOTAL_SIZE // 2, TOTAL_SIZE, TOTAL_SIZE,
                                     color=arcade.color.LIGHT_GRAY)
        arcade.draw_rectangle_filled((TOTAL_SIZE // 2) + 400, TOTAL_SIZE // 2, TOTAL_SIZE - 400, TOTAL_SIZE,
                                     color=arcade.color.LIGHT_GOLDENROD_YELLOW)
        arcade.draw_texture_rectangle(TOTAL_SIZE // 2, TOTAL_SIZE // 2, TOTAL_SIZE, TOTAL_SIZE,
                                      arcade.load_texture("chess_board.png"))

        for i in range(8):
            for j in range(8):
                if board.board[i][j] != 'e':
                    x = (j * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)
                    y = (i * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)
                    arcade.draw_texture_rectangle(x, y, (TOTAL_SIZE / 8), (TOTAL_SIZE / 8),
                                                  arcade.load_texture(
                                                      "sprites/" + SPRITE_MAP[board.board[i][j]] + ".png"))

        if self.selection:
            arcade.draw_rectangle_outline(self.sy + 1, self.sx, (TOTAL_SIZE / 8) - 3, (TOTAL_SIZE / 8) - 3,
                                          arcade.color.GREEN, 4)
            for i in self.pos_mov:
                x = (i[0] * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)
                y = (i[1] * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)
                if board.board[i[0]][i[1]] != 'e':
                    arcade.draw_ellipse_outline(y, x, (TOTAL_SIZE / 8), (TOTAL_SIZE / 8),
                                                arcade.color.RED, tilt_angle=0, border_width=4, num_segments=6)
                else:
                    arcade.draw_circle_filled(y, x, 5, arcade.color.GREEN)

    def on_mouse_press(self, x, y, button, modifiers):
        ay = int(x / (TOTAL_SIZE/8))  # row value for piece array
        ax = int(y / (TOTAL_SIZE/8))  # column value for piece array
        if x < 600:
            if board.pieces[ax][ay] != 'e':
                if board.pieces[ax][ay].white and self.turn:
                    pass
                elif not board.pieces[ax][ay].white and not self.turn:
                    pass
                elif board.pieces[ax][ay].white and not self.turn and self.selection:
                    moved = board.move(self.px, self.py, ax, ay)
                    self.selection = False
                    self.pos_mov = []
                    if moved:
                        self.turn = not self.turn
                    return
                elif not board.pieces[ax][ay].white and self.turn and self.selection:
                    moved = board.move(self.px, self.py, ax, ay)
                    self.selection = False
                    self.pos_mov = []
                    if moved:
                        self.turn = not self.turn
                    return
                else:
                    self.selection = False
                    return
            if not self.selection:
                if board.board[ax][ay] != 'e':
                    self.px = ax
                    self.py = ay
                    board.pieces[self.px][self.py].selected = True
                    self.pos_mov = board.pieces[ax][ay].valid_moves(board.pieces)
                    print(self.pos_mov)
                    self.sx, self.sy = calculate_coordinates(ax, ay)
                    self.selection = True
            else:
                moved = board.move(self.px, self.py, ax, ay)
                self.selection = False
                self.pos_mov = []
                if moved:
                    self.turn = not self.turn
            if len(self.pos_mov) == 0:
                self.selection = False


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
