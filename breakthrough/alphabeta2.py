import board
import breakthrough
import heuristics

# different pieces/players
WHITE = 0
BLACK = 1

def alphabeta(curr_board, turn, end_game, depth, max_player, score, nodes_expanded, alpha, beta):

    """
    :param curr_board: current state of the board
    :param turn: which player's turn it is
    :param end_game: boolean that says whether the game is over
    :param depth: depth of alphabeta tree
    :param max_player: boolean that says whether we're calculating the max or min score
    :param score: score for each move given by the heuristic
    :return: piece to move and the position it should move to
    """
    if depth == 0 or end_game is True:
        return score, None, None, None, nodes_expanded, alpha, beta

    # switches turn for recursive call
    new_turn = turn
    if new_turn == WHITE:
        new_turn = BLACK
    else:
        new_turn = WHITE

    if max_player:
        # initialize values
        best_val = -1000
        best_piece = None
        best_x_move = None
        best_y_move = None
        new_board = board.Board()

        for piece in curr_board.alive_pieces:
            if piece.color != turn:
                continue

            # goes through all possible 6 moves for each piece
            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y-1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1, alpha, beta)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break


            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1, alpha, beta)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1, alpha, beta)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y-1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1, alpha, beta)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1, alpha, beta)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1, alpha, beta)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break

        return best_val, best_piece, best_x_move, best_y_move, nodes_expanded, alpha, beta

    else:
        # initialize values
        best_val = 1000
        new_board = board.Board()
        best_piece = None
        best_x_move = None
        best_y_move = None

        for piece in curr_board.alive_pieces:
            if piece.color != turn:
                continue

            # goes through all possible 6 moves for each piece
            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y-1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1, alpha, beta)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                beta = min(beta, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1, alpha, beta)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                beta = min(beta, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1, alpha, beta)
                best_val = min(best_val, val)
                best_val = min(best_val, val, alpha, beta)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                beta = min(beta, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y-1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1, alpha, beta)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                beta = min(beta, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1, alpha, beta)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                beta = min(beta, best_val)
                if beta <= alpha:
                    break

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.defensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded, alpha, beta = alphabeta(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1, alpha, beta)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y
                beta = min(beta, best_val)
                if beta <= alpha:
                    break

        return best_val, best_piece, best_x_move, best_y_move, nodes_expanded, alpha, beta
