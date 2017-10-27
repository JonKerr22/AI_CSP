class Path:
	def __init__(self, startPoint=None, endPoint=None, color=None):
		if(startPoint is None):
			self.startPoint = (-1,-1)
			self.endPoint = (-1,-1)
			self.color = ''
		else:
			self.startPoint = startPoint
			self.endPoint = endPoint
			self.color = color
		self.path = [(startPoint)] 

	def __str__(self):
		return self.path

	def containsZigZag(self):
		for coord in self.path: #zigzag check loop
			if (coord[0] +1, coord[1]) in self.path and (coord[0] -1, coord[1]) in self.path and (coord[0], coord[1]+1) in self.path:
				return True
			elif (coord[0] +1, coord[1]) in self.path and (coord[0] -1, coord[1]) in self.path and (coord[0], coord[1]-1) in self.path:
				return True
			elif (coord[0] +1, coord[1]) in self.path and (coord[0], coord[1]-1) in self.path and (coord[0], coord[1]+1) in self.path:
				return True
			elif (coord[0] -1, coord[1]) in self.path and (coord[0], coord[1]-1) in self.path and (coord[0], coord[1]+1) in self.path:
				return True
		return False

	def newPathPlusMove(self, x, y):
		p = Path(self.startPoint, self.endPoint, self.color)
		if (x,y) not in self.path:
			p.path = self.path + [(x,y)]
		return p
	
	def deepCopy(self, path):
		self.startPoint = path.startPoint
		self.endPoint = path.endPoint
		self.color = path.color
		self.path = path.path