from path import Path
from Queue import Queue

POSSIBLE_MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

class Search:
	def __init__(self, board, start, end, color):
		self.board = board
		self.boardSize = len(board[0])-1
		self.startPoint = start
		self.endPoint = end
		self.color = color

	def searchForAllPaths(self):

		completePaths = []
		inProgressPath = Path(self.startPoint, self.endPoint, self.color)

		frontier = Queue()
		visited = [self.startPoint]
		for move in self.getMoves(self.startPoint[0], self.startPoint[1]):
			frontier.put(move)
		while len(frontier.queue) > 0: 
			curr = frontier.get()
			if(curr in visited):
				continue
			visited.append(curr)
			inProgressPath.path.append(curr) #BUG: currently saves all moves, 
											 #should be multiple paths not sure how yet
			if(curr == self.endPoint):
				#print(str(inProgressPath.path))
				completePaths.append(inProgressPath)
			else:
				for move in self.getMoves(curr[0], curr[1]):
					frontier.put(move)

		return completePaths


	def getMoves(self, x, y):
		moves = []
		for move in POSSIBLE_MOVES:
			if self.inBound(x+move[0], y+move[1]):
				if self.board[x+move[0]][y+move[1]] == '_' or (x+move[0], y+move[1]) == self.endPoint:
					moves.append((x+move[0],y+move[1]))

		return moves

	def inBound(self, x,y):
		return x >= 0 and y >= 0 and x<self.boardSize and y<self.boardSize
