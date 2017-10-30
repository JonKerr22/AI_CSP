# different pieces/players
WHITE = 0
BLACK = 1

class Piece:

    def __init__(self):
        self.color = None
        self.x = None
        self.y = None

    def move(self, new_y, new_x, board, alive_pieces, turn):
        """
        :param new_x: new x coordinate on board to move to
        :param new_y: new y coordinate on board to move to
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
        elif (turn == WHITE and self.y - new_y == 1) or (turn == BLACK and self.y - new_y == -1):   # invalid movements
            return False
        elif abs(self.x - new_x) > 1:
            return False
        elif self.x == new_x:   # can't move straight if another piece is blocking
            new_spot = board[new_y][new_x]
            if new_spot is not None:
                return False
            else:
                board[self.y][self.x] = None
                board[new_y][new_x] = self
                self.x = new_x
                self.y = new_y
                return True
        else:   # diagonals
            new_spot = board[new_y][new_x]
            if new_spot is not None:    # other piece in that spot
                if new_spot.color == self.color:   # can't kill your own player
                    return False
                else:   # kill move
                    alive_pieces.remove(new_spot)
                    board[self.y][self.x] = None
                    board[new_y][new_x] = self
                    self.x = new_x
                    self.y = new_y
                    return True
            else:
                board[self.y][self.x] = None
                board[new_y][new_x] = self
                self.x = new_x
                self.y = new_y
                return True