from pieces import piece
import copy

class King(piece.Piece):
    def __init__(self, px, py, color):
        super().__init__(px, py, color)

    def valid_moves(self, board):
        moves = []
        inv_moves = []  # invalid moves, in other words, moves that put the king in check or checkmate

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

        for i in range(8):
            for j in range(8):
                if board[i][j] != 'e' and type(board[i][j]) != type(self) and board[i][j].white != self.white:
                    for mov in moves:
                        aux = copy.deepcopy(board)
                        aux[mov[0]][mov[1]] = aux[self.pos_x][self.pos_y]
                        aux[self.pos_x][self.pos_y] = 'e'
                        apm = aux[i][j].valid_moves(aux)
                        if mov in apm:
                            inv_moves.append(mov)
                        if len(inv_moves) == len(moves):
                            return []

        moves = [x for x in moves if x not in inv_moves]

        return moves
