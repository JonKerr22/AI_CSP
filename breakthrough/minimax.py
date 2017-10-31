import board
import breakthrough
import heuristics

def minimax(curr_board, turn, end_game, depth, max_player, score, nodes_expanded):
    """
    :param curr_board: current state of the board
    :param turn: which player's turn it is
    :param end_game: boolean that says whether the game is over
    :param depth: depth of minimax tree
    :param max_player: boolean that says whether we're calculating the max or min score
    :param score: score for each move given by the heuristic
    :param nodes_expanded: total times minimax function has been called per move (increments by 1 each time)
    :return: piece to move and the position it should move to and the total nodes expanded
    """

    if depth == 0 or end_game is True:
        return score, None, None, None, nodes_expanded

    # switches turn for recursive call
    new_turn = turn
    if new_turn == 0:
        new_turn = 1
    else:
        new_turn = 0

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
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y-1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth-1, False, move_score, nodes_expanded+1)
                best_val = max(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

        return best_val, best_piece, best_x_move, best_y_move, nodes_expanded

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
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x-1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y-1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

            new_board = curr_board.copy_board(new_board)
            new_piece = new_board.board[piece.x][piece.y]
            successful_move = new_piece.move(piece.x+1, piece.y+1, new_board.board, new_board.alive_pieces, turn)
            if successful_move:
                move_score = heuristics.offensive1(turn, new_board)
                val, curr_best_piece, curr_best_x_move, curr_best_y_move, nodes_expanded = minimax(new_board, new_turn, breakthrough.game_over(piece), depth - 1, True, move_score, nodes_expanded+1)
                best_val = min(best_val, val)
                if best_val == val:
                    best_piece = piece
                    best_x_move = new_piece.x
                    best_y_move = new_piece.y

        return best_val, best_piece, best_x_move, best_y_move, nodes_expanded