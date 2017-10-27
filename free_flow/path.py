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
		self.path = (startPoint) #should be a list of tuples

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

	