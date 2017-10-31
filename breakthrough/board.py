import gamePiece

# different pieces/players
WHITE = 0
BLACK = 1

class Board:
    def __init__(self):
        self.board = []  # game board
        self.alive_pieces = []  # keeps track of alive pieces in current game

    def set_board(self):
        """sets board up in beginning of the game"""
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

    def copy_board(self, new_board):
        """copies current state of the board to a new board"""
        for i in range(0, 8):
            board_cols = []
            for j in range(0, 8):
                if self.board[i][j] is not None:
                    new_piece = gamePiece.Piece()
                    new_piece.color = self.board[i][j].color
                    new_piece.x = self.board[i][j].x
                    new_piece.y = self.board[i][j].y
                    board_cols.append(new_piece)
                    new_board.alive_pieces.append(new_piece)
                else:
                    board_cols.append(None)
            new_board.board.append(board_cols)
        return new_board

    def print_board(self):
        """prints board state"""
        curr_line = "|"
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] is None:
                    curr_line += ' |'
                elif self.board[i][j].color == WHITE:
                    curr_line += 'W|'
                elif self.board[i][j].color == BLACK:
                    curr_line += 'B|'
                else:
                    curr_line += ' '
            print(curr_line)
            curr_line = "|"

    def pieces_left(self, color):
    	left = 0
    	for i in range(0, 8):
            for j in range(0, 8):
            	if self.board[i][j] == color:
            		left +=1
        return left