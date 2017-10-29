#offensive heuristic 2: try and find moves that max the number of pieces you attack
	#defense 1 just defends itself doesn't attack your pieces, so offense 2 beats it

#defensive heuristic 2: try to bait offensive 1 to attack for no gain, in order to open up
	#more paths to opponent home row, not yet sure exactly how to choose where to bait opponent

import gamePiece

# different pieces/players
WHITE = 0
BLACK = 1

class Board:

    def __init__(self):
        self.board = []  # game board
        self.alive_pieces = []  # keeps track of alive pieces in current game

    def set_board(self):
        for i in range(0, 8):
            board_cols = []
            for j in range(0, 8):
                if i == 0 or i == 1:
                    new_piece = gamePiece.Piece()
                    new_piece.color = WHITE
                    new_piece.x = j
                    new_piece.y = i
                    board_cols.append(new_piece)
                    self.alive_pieces.append(new_piece)
                elif i == 6 or i == 7:
                    new_piece = gamePiece.Piece()
                    new_piece.color = BLACK
                    new_piece.x = j
                    new_piece.y = i
                    board_cols.append(new_piece)
                    self.alive_pieces.append(new_piece)
                else:
                    board_cols.append(None)
            self.board.append(board_cols)

    def print_board(self):
        print(len(self.board[0]))
        currLine = "|"
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] is None:
                    currLine += ' |'
                elif self.board[i][j].color == WHITE:
                    currLine += 'W|'
                elif self.board[i][j].color == BLACK:
                    currLine += 'B|'
                else:
                    currLine += ' '
            print(currLine)
            currLine = "|"