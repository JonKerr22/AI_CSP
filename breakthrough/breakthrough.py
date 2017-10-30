import board
import gamePiece
import minimax

# different pieces/players
WHITE = 0
BLACK = 1

def game_over(piece_moved):
    """
    :param piece_moved: last piece moved on board
    :return: true or false depending on if the game is over

    Game is over when one player's piece reaches the opposite side of the board.
    Checks to see if the last piece moved was moved to end row.
    """
    if piece_moved.color == WHITE:
        if piece_moved.y == 7:
            return True
    elif piece_moved.color == BLACK:
        if piece_moved.y == 0:
            return True
    return False

def game_play():
    """runs through game"""
    game_board = board.Board()
    game_board.set_board()
    turn = WHITE  # which player's turn it is

    while 1:  # game loop
        # call heuristic functions
        score, piece_to_move, piece_x, piece_y = minimax.minimax(game_board, turn, False, 3, True, 0)
        piece_to_move.move(piece_to_move, piece_y, piece_x, game_board.board, game_board.alive_pieces, turn)
        game_board.print_board()

        # breaks from loop when game is over
        if game_over(piece_to_move):
            break

        # switches players turn
        if turn == WHITE:
            turn = BLACK
        else:
            turn = WHITE

if __name__ == '__main__':
    game_play()