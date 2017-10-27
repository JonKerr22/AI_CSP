from path import Path
from Queue import Queue

POSSIBLE_MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

class Search:
	def __init__(self, board, start, end, color):
		self.board = board
		self.boardSize = len(board[0])
		self.startPoint = start
		self.endPoint = end
		self.color = color

	def searchForAllPaths(self):
		completePaths = ()
		pathsInProgress = ()

	def getMoves(self, x, y):
		moves = []
		for move in POSSIBLE_MOVES:
			if self.inBound(x+move[0], y+move[1]) and self.board[x+move[0]][y+move[1]] == '_':
				moves.append((x+move[0],y+move[1]))

		return moves

	def inBound(self, x,y):
		return x >= 0 and y >= 0 and x<self.boardSize and y<self.boardSize
