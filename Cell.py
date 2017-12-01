class Cell:

	def __init__(self, x, y):
		self.x 			= x
		self.y 			= y
		self.visited	= False
		self.current	= False
		self.empty		= False # Wall(False) or Empty(True)
		self.name		= "["+str(x)+","+str(y)+"]"

	def get_name(self):
		return self.name

	def marked(self):
		self.empty=False

	def current_vist(self):
		self.current=True

	def is_visited(self):
		return self.visited

	def end_walk(self):
		self.visited=True

	def print_cell_info(self):
		print "Cell", self.name, "at ", self.x, ",", self.y, "and it is visited,",self.visited,"is marked",self.empty