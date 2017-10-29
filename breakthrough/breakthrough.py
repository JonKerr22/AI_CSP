import board

# different pieces/players
WHITE = 0
BLACK = 1

def game_play(self):
    game_board = board.Board()
    game_board.set_board()
    turn = WHITE  # which player's turn it is

    while 1:  # game loop
        # call heuristic functions

        # switches players turn
        if turn == WHITE:
            turn = BLACK
        else:
            turn = WHITE

currBoard = board.Board()
currBoard.set_board()
currBoard.print_board()