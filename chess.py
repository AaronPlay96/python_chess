import arcade
from board import Board

TOTAL_SIZE = 600  #the size of the chess table with the image borders, the black lineas around the image.
TABLE_SIZE = 600  #the size of the chess table without the image borders.
SCREEN_TITLE = 'CHESS'
SPRITE_MAP = {'p': 'whitePawn', 'r': 'whiteRook', 'n': 'whiteKnight',
              'b': 'whiteBishop', 'q': 'whiteQueen', 'k': 'whiteKing',
              'P': 'blackPawn', 'R': 'blackRook', 'N': 'blackKnight',
              'B': 'blackBishop', 'Q': 'blackQueen', 'K': 'blackKing'}
board = Board()


class MyGame(arcade.Window):
    global board
    global TOTAL_SIZE

    def __init__(self):
        super().__init__(TOTAL_SIZE, TOTAL_SIZE, SCREEN_TITLE)
        self.set_mouse_visible(True)
        self.sx = -10
        self.sy = -10
        self.selection = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(TOTAL_SIZE // 2, TOTAL_SIZE // 2, TOTAL_SIZE, TOTAL_SIZE,
                                     color=arcade.color.LIGHT_BROWN)
        arcade.draw_texture_rectangle(TOTAL_SIZE // 2, TOTAL_SIZE // 2, TOTAL_SIZE, TOTAL_SIZE,
                                      arcade.load_texture("chess_board.png"))

        # arcade.draw_rectangle_filled(115,115,(TOTAL_SIZE / 8), (TOTAL_SIZE / 8), color=arcade.color.GREEN)

        for i in range(8):
            for j in range(8):
                if board.board[i][j] != 'e':
                    x = (j * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)
                    y = (i * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)
                    arcade.draw_texture_rectangle(x, y, (TOTAL_SIZE / 8), (TOTAL_SIZE / 8),
                                                  arcade.load_texture(
                                                      "sprites/" + SPRITE_MAP[board.board[i][j]] + ".png"))

        if self.selection:
            arcade.draw_rectangle_outline(self.sy, self.sx, (TOTAL_SIZE / 8), (TOTAL_SIZE / 8), arcade.color.GREEN, 4)

    def calculate_coordinates(self, sx, sy):
        return [((sx * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)), ((sy * (TABLE_SIZE / 8)) + (TABLE_SIZE / 16)), True]

    def on_mouse_press(self, x, y, button, modifiers):
        self.sy = int(x / (TOTAL_SIZE/8))
        self.sx = int(y / (TOTAL_SIZE/8))
        print(str(self.sx) + " " + str(self.sy))
        if not self.selection and board.board[self.sx][self.sy] != 'e':
            self.sx, self.sy, self.selection = self.calculate_coordinates(self.sx, self.sy)
        elif self.selection and board.board[self.sx][self.sy] != 'e':
            self.sx, self.sy, self.selection = self.calculate_coordinates(self.sx, self.sy)
        else:
            self.selection = False


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()