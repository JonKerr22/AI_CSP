from random import *

# different pieces/players
WHITE = 0
BLACK = 1

def number_of_pieces(color, alive_pieces):
    """
    :param color: which color's pieces you're counting
    :param alive_pieces: array with all the current alive pieces on the board
    :return: number of alive pieces of a certain color

    Finds number of pieces left on the board of a certain color.
    """
    counter = 0
    for piece in alive_pieces:
        if piece.color == color:
            counter += 1
    return counter

def offensive1(player, board):
    """
    :param player: color of the player whose turn it is
    :param board: current state of the board
    :return: score for each move (higher is better)

    The more pieces your opponent has, the lower the score will be.
    """

    if player == WHITE:     # find number of opponent's pieces
        num_pieces = number_of_pieces(BLACK, board.alive_pieces)
    else:
        num_pieces = number_of_pieces(WHITE, board.alive_pieces)

    return 2 * (30 - num_pieces) + random()

def defensive1(player, board):
    """
    :param player: color of the player whose turn it is
    :param board: current state of the board
    :return: score for each move (higher is better)

    The more pieces you opponent have, the higher the score will be.
    """

    num_pieces = number_of_pieces(player, board.alive_pieces)   # find number of your pieces

    return 2 * num_pieces + random()

def offensive2(player, board):
	"""
	Goal is to beat defensive1, which seeks to maximize 
	the number of it's own peices. So to beat that, goal
	is to maximize number of peices you can attack, since defensive 
	one doesn't avoid moving into attack, just avoids losing
	"""
	
def defensive2(player, board):
	"""
	Goal is to beat offensive1, which seeks to lower
	the total number of peices your opponenet has. To
	beat that try and minimize the number of peices that
	other player can attack with, basically avoid being diagonal 
	from an opponent peice, but try and get your pieces directly 
	in front of opponent
	"""