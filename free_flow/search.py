from path import Path
from Queue import Queue
from collections import defaultdict
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
		incompletePaths = []
		existingPaths = defaultdict(bool)
		inProgressPath = Path(self.startPoint, self.endPoint, self.color)
		incompletePaths.append(inProgressPath) 

		frontier = Queue()
		visited = [self.startPoint]
		prev = self.startPoint
		for move in self.getMoves(self.startPoint[0], self.startPoint[1]):
			frontier.put(move)
		while len(frontier.queue) > 0: 
			curr = frontier.get()
#			if(curr in visited):
#				continue
			visited.append(curr)
			#print(mDistance(curr[0], prev[0], curr[1], prev[1]))
			if mDistance(curr[0], prev[0], curr[1], prev[1]) == 1: #in same path as previous
				if curr not in inProgressPath.path:
					inProgressPath.path.append(curr)
			else:
				#print("previous:"+ str(prev) +"at: " + str(curr)+ ", old path: "+ str(inProgressPath.path))
				#save old path
				incompletePaths.append(inProgressPath)
				#if new path right next to start node, then get new path and start that
				if mDistance(curr[0], self.startPoint[0], curr[1], self.startPoint[1]) == 1:					
					start = Path(self.startPoint, self.endPoint, self.color)
					#print("new from start: "+ str(start.path))
					inProgressPath = start.newPathPlusMove(curr[0], curr[1])
					#print("new path: " + str(inProgressPath))
				#go through incompletePaths to find which one this is a part of, append to that
				else:
					#print("continued path from these: " + str(incompletePaths))
					for path in incompletePaths:
						x2,y2 = path.path[-1]
						if mDistance(curr[0], x2, curr[1], y2) == 1:
							inProgressPath = path.newPathPlusMove(curr[0], curr[1])
							break
			
											
			if(curr == self.endPoint):
				#print(str(inProgressPath.path))
				completePaths.append(inProgressPath)
			else:
				if existingPaths[tuple(inProgressPath.path)]:
					continue
				print(tuple(inProgressPath.path),"\n")
				existingPaths[tuple(inProgressPath.path)] = True
				for move in self.getMoves(curr[0], curr[1]):
					frontier.put(move)

			if inProgressPath.path is None:
				print("ring ring")
			prev = curr
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










def mDistance(x1, x2, y1, y2):
	return abs(x1 - x2) + abs(y1 - y2)
