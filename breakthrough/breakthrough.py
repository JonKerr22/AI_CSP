import board
import minimax
import time

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
        if piece_moved.x == 7:
            return True
    elif piece_moved.color == BLACK:
        if piece_moved.x == 0:
            return True
    return False

def game_play():
    """runs through game"""
    game_board = board.Board()
    game_board.set_board()
    turn = WHITE  # which player's turn it is
    num_moves = 0
    time_per_move = []
    nodes_per_move = []
    black_nodes_expanded = 0
    white_nodes_expanded = 0

    while 1:  # game loop
        start_time = time.time()
        # call heuristic functions
        score, piece_to_move, piece_x, piece_y, nodes_expanded = minimax.minimax(game_board, turn, False, 3, True, 0, 0)

        if piece_to_move is None:   # edge case where all pieces of certain color are killed
            if turn == WHITE:
                player = "black"
            else:
                player = "white"
            print("Winner is: " + player)
            print("Average time per move: " + str(sum(time_per_move)/len(time_per_move)))
            print("Average nodes per move: " + str(sum(nodes_per_move)/len(nodes_per_move)))
            print("Nodes expanded by white: " + str(white_nodes_expanded))
            print("Nodes expanded by black: " + str(black_nodes_expanded))
            break

        piece_to_move.move(piece_x, piece_y, game_board.board, game_board.alive_pieces, turn)

        # calculations for report
        nodes_per_move.append(nodes_expanded)
        if turn == WHITE:
            white_nodes_expanded += nodes_expanded
        else:
            black_nodes_expanded += nodes_expanded
        end_time = time.time()
        time_per_move.append(end_time-start_time)
        num_moves += 1

        game_board.print_board()
        print("\n")
        print('----------------------------')
        print("\n")

        # breaks from loop when game is over
        if game_over(piece_to_move):
            if turn == WHITE:
                player = "white"
            else:
                player = "black"
            print("Winner is: " + player)
            print("Average time per move: " + str(sum(time_per_move) / len(time_per_move)))
            print("Average nodes per move: " + str(sum(nodes_per_move) / len(nodes_per_move)))
            print("Nodes expanded by white: " + str(white_nodes_expanded))
            print("Nodes expanded by black: " + str(black_nodes_expanded))
            break

        # switches players turn
        if turn == WHITE:
            turn = BLACK
        else:
            turn = WHITE

if __name__ == '__main__':
    game_play()
