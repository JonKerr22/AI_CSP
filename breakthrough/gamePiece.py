class Piece:

    def __init__(self):
        self.color = None
        self.x = None
        self.y = None

    # moves piece to different square on board
    def move(self, new_x, new_y, board, alive_pieces):
        if new_x == self.x and new_y == self.y:   # same spot
            return False
        elif new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:    # off board
            return False
        elif abs(self.y - new_y) != 1:   # invalid movements
            return False
        elif abs(self.x - new_y) > 1:
            return False
        elif self.x == new_x:   # can't move straight if another piece is blocking
            new_spot = board[new_x][new_y]
            if new_spot is not None:
                return False
            else:
                board[self.x][self.y] = None
                board[new_x][new_y] = self
                return True
        else:   # diagonals
            new_spot = board[new_x][new_y]
            if new_spot is not None:    #other piece in that spot
                if new_spot.color == self.color:   # can't kill your own player
                    return False
                else:   # kill move
                    alive_pieces.remove(new_spot)
                    board[self.x][self.y] = None
                    board[new_x][new_y] = self
                    return True
            else:
                board[self.x][self.y] = None
                board[new_x][new_y] = self
                return True