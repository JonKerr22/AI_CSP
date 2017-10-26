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
		return (startCoords, endCoords)
	def isPathLegal(self):
		i=0
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

g = Game("input55.txt")
g.printColors()
g.printBoard()
for c in g.colors:
	print(c + " " + str(g.generateAllPaths_oneColor(c)))