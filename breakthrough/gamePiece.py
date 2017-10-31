# different pieces/players
WHITE = 0
BLACK = 1

class Piece:

    def __init__(self):
        self.color = None
        self.x = None
        self.y = None

    def move(self, new_x, new_y, board, alive_pieces, turn):
        """
        :param new_x: new x coordinate on board to move to (row)
        :param new_y: new y coordinate on board to move to (column)
        :param board: current state of the game board
        :param alive_pieces: list of alive pieces on the board
        :param turn: which players turn it is
        :return: true or false based on whether the move is legal

        Moves a piece from one square to another.
        """
        if turn != self.color:
            return False
        elif new_x == self.x and new_y == self.y:   # same spot
            return False
        elif new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:    # off board
            return False
        elif (turn == WHITE and self.x - new_x == 1) or (turn == BLACK and self.x - new_x == -1):   # invalid movements
            return False
        elif abs(self.y - new_y) > 1:
            return False
        elif self.y == new_y:   # can't move straight if another piece is blocking
            new_spot = board[new_x][new_y]
            if new_spot is not None:
                return False
            else:
                board[self.x][self.y] = None
                board[new_x][new_y] = self
                self.x = new_x
                self.y = new_y
                return True
        else:   # diagonals
            new_spot = board[new_x][new_y]
            if new_spot is not None:    # other piece in that spot
                if new_spot.color == self.color:   # can't kill your own player
                    return False
                else:   # kill move
                    alive_pieces.remove(new_spot)
                    board[self.x][self.y] = None
                    board[new_x][new_y] = self
                    self.x = new_x
                    self.y = new_y
                    return True
            else:
                board[self.x][self.y] = None
                board[new_x][new_y] = self
                self.x = new_x
                self.y = new_y
                return True

    def is_attackable(self, board):
        if self.color == WHITE:
            for piece in board.alive_pieces:
                if piece.color == BLACK and ((piece.x == self.x-1 or piece.x == self.x+1) and piece.y == self.y+1):
                    return True
        else:
            for piece in board.alive_pieces:
                if piece.color == WHITE and ((piece.x == self.x-1 or piece.x == self.x+1) and piece.y == self.y-1):
                    return True
        return False

    def unable_to_attack(self, board):
        if self.color == WHITE:
            #on left wall
            if self.x == 0 and (board[self.x+1][self.y+1] is None or board[self.x+1][self.y+1].color == WHITE):
                return False
            #on right wall
            elif self.x == 7 and (board[self.x-1][self.y+1] is None or board[self.x-1][self.y+1].color == WHITE):
                return False
            elif (board[self.x-1][self.y+1] is None or board[self.x-1][self.y+1].color == WHITE) and (board[self.x+1][self.y+1] is None or board[self.x+1][self.y+1].color == WHITE):
                return False
        else:
            #on left wall
            if self.x == 0 and (board[self.x+1][self.y-1] is None or board[self.x+1][self.y-1].color == BLACK):
                return False
            #on right wall
            elif self.x == 7 and (board[self.x-1][self.y-1] is None or board[self.x-1][self.y-1].color == BLACK):
                return False
            elif (board[self.x-1][self.y-1] is None or board[self.x-1][self.y-1].color == BLACK) and (board[self.x+1][self.y-1] is None or board[self.x+1][self.y-1].color == BLACK):
                return False

        return True