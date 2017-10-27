from path import Path
from Queue import Queue

class Search:
	def __init__(self, board, start, end, color):
		self.board = board
		self.startPoint = start
		self.endPoint = end
		self.color = color

	def searchForAllPaths(self):
		completePaths = ()
		pathsInProgress = ()

