from path import Path
from search import Search

POSSIBLE_MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

class Game:
	def __init__(self, inputFile):
		self.inputFile = inputFile
		self.board = []
		self.boardSize = int(inputFile[5]) #input file names all have same format
		self.solveTime = 0
		colors = []
		textFile = open(self.inputFile)
		lines = textFile.readlines()
		for l in lines:
			charLine = list(l)
			self.board.append(charLine)
			for c in charLine:
				if(c.isupper() and c not in colors):
					colors.append(c)
		self.colors = colors


	def dumbSolve(self):
		i=0
		#attempt move
		#check constraints
		#if move valid, do move
		#see if solved for 1 color
			#see if solved for whole board
			#check if solution prevents other solutions from happening
				#if solution is too constraining, throw out try again

		#uninformed search, probably just modify part of mp1
	
	def smartSolve(self):
		i=0

	def generateAllPaths_oneColor(self, color):
		startCoords = (-1,-1)
		endCoords = (-1,-1)
		for i in range(self.boardSize):
			for j in range(self.boardSize):
				if self.board[i][j] == color:
					if(startCoords[0] == -1):
						startCoords = (i,j)
					else:
						endCoords = (i,j)
		searcher = Search(self.board, startCoords, endCoords, color)
		paths = searcher.searchForAllPaths()#BUG: only finding 1 path
		legalPaths = filter(lambda path : self.isPathLegal(path), paths)
		return legalPaths

	def isPathLegal(self, path):#should include Path object
		if path.startPoint == (-1,-1) or path.containsZigZag() or self.anySourceBlocked():
			return False
		return True

	def findSolution(self):
		#search all paths that all the colors can have, find the ones that don't overlap\
		i=0
	def printColors(self):
		for c in self.colors:
			print(c)
	def printBoard(self):
		for line in self.board:
			row = ""
			for char in line:
				if(char != '\n'):
					row += char
			print row
	def anySourceBlocked(self):
		for i in range(self.boardSize):
			for j in range(self.boardSize):
				if self.board[i][j] != '_' and self.coordBlocked(i,j):
					return True
		return False

	def coordBlocked(self, x,y) :
		if self.board[x][y] == '_':
			return False
		color = self.board[x][y]
		for move in POSSIBLE_MOVES:
			if self.inBound(x+move[0], y+move[1]) and (self.board[x+move[0]][y+move[1]] == '_' or self.board[x+move[0]][y+move[1]] == color):
				return False
		return True


	def inBound(self, x,y):
		return x >= 0 and y >= 0 and x<self.boardSize and y<self.boardSize



g = Game("input77.txt")
g.printBoard()

#print(g.anySourceBlocked())
#print('B' + " " + str(g.generateAllPaths_oneColor('B')))
for c in g.colors:
	path = g.generateAllPaths_oneColor(c)[0]
	print(c + " " + str(path.path))
