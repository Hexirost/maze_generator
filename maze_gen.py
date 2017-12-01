import pygame
from Cell import Cell

HORIZONTAL 	= 5
VERTICAL 	= 5

def maze_walk(node,current_walk):
	while(True):
		edge_choice=[]
		if node.is_visited() == True:
			try:
				current_walk.remove(node)
			except:
				print "DOES IT EVER GO HERE?"
				pass
			return

		# North
		if not grid[node.x+2][node.y].current_vist():
			edge_choice.append(grid[node.x+2][node.y])

		# if node is south

		# if node is east

		# if node is west

		if len(edge_choice) != 0:
			next_node = random.choice(edge_choice)
			print "Cell",node.get_name(),"is visiting",next_node.get_name()
			node.current_vist()
			if node not in current_walk:
				current_walk.append(node)
			maze_walk(next_node,current_walk)
		else:
			node.end_walk()
			break
	return current_walk

grid_len   = HORIZONTAL*2+1 
grid_width = VERTICAL*2+1

grid = [[None for x in range(grid_len)] for y in range(grid_width)]

for n in range(grid_len):
	for m in range(grid_width):
		new_cell = Cell(m,n)
		grid[m][n]=new_cell
		# new_cell.print_cell_info()


