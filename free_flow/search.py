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
		base = inProgressPath.deepCopy()
		incompletePaths.append(base) 

		frontier = Queue()
		prev = self.startPoint
		for move in self.getMoves(self.startPoint[0], self.startPoint[1]):
			frontier.put(move)
		minLength = 1
		frontierLoops = 0
		while len(frontier.queue) > 0:
			#min path exists to prevent creation of repeat paths
			frontierLoops+=1
			if(frontierLoops==len(self.getMoves(self.startPoint[0], self.startPoint[1]))+1):
				minLength = 2
			if(frontierLoops == 4*len(self.getMoves(self.startPoint[0], self.startPoint[1]))+1):
				minLength = 3

			curr = frontier.get()
			if(curr in inProgressPath.path):#don't have paths backtrace on self
				continue
			print("at: "+str(curr))

			if mDistance(curr[0], prev[0], curr[1], prev[1]) == 1: #in same path as previous
				inProgressPath = inProgressPath.newPathPlusMove(curr[0], curr[1])
				
				print("same path: " + str(inProgressPath.path))
				if curr == self.endPoint :
					completePaths.append(inProgressPath.deepCopy())
					print("found complete: "+ str(inProgressPath.path))
			else:
				#save old path
				temp = inProgressPath.deepCopy()
				incompletePaths.append(temp)
		
				#go through incompletePaths to find which one this is a part of, append to that
				for path in incompletePaths:
					print("checking this path: "+str(path.path))
					x2,y2 = path.path[-1]
					#print("at: " + str(curr)+ "looking at: " + str((x2,y2)) + "distance: " + str(mDistance(curr[0], x2, curr[1], y2)))
					#print(mDistance(curr[0], x2, curr[1], y2))
					if mDistance(curr[0], x2, curr[1], y2) == 1 and len(path.path)>=minLength:
				#		print("found new!")
						path = path.newPathPlusMove(curr[0], curr[1])
						inProgressPath = path.deepCopy()
						if curr == self.endPoint :
							completePaths.append(inProgressPath.deepCopy()) 
							print("found complete: "+ str(inProgressPath.path))

						
				print("switched to path: " + str(inProgressPath.path))
											
			if(curr == self.endPoint):
				#print("found complete: "+ str(inProgressPath.path))
				prev = (-2, -2) #set to outside board mdistance of 1
				#completePaths.append(inProgressPath.deepCopy())
				if(len(incompletePaths) > 0):
					inProgressPath = incompletePaths[-1]
				continue
			else:
				print(tuple(inProgressPath.path),"\n")
				if existingPaths[tuple(inProgressPath.path)]:
					continue
				
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
