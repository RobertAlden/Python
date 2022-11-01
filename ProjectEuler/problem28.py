grid_size = 1001

grid = list()
for i in range(grid_size):
	new_list = [0] * grid_size
	grid.append(new_list)

direction = 0

def set_grid(x,y,n):
	grid[y][x] = n

def get_grid(x,y):
	return grid[y][x]

def print_grid():
	for y in range(grid_size):
		for x in range(grid_size):
			print(get_grid(x,y), end = " ")
		print("")

#print_grid()

def fill_grid(g):
	value = grid_size**2
	x = grid_size
	y = 0
	direction = 2
	travel = grid_size
	while value > 0:
		#print(value)
		
		if direction == 0:
			x+=1
			if not (x < 0 or x == grid_size or y < 0 or y == grid_size):
				if get_grid(x,y) == 0:
					set_grid(x,y,value)
					value -= 1
				else:
					x-=1
					direction += 1
					if direction == 4:
						direction = 0
			else:
				x-=1
				direction += 1
				if direction == 4:
					direction = 0
		elif direction == 1:
			y-=1
			if not (x < 0 or x == grid_size or y < 0 or y == grid_size):
				if get_grid(x,y) == 0:
					set_grid(x,y,value)
					value -= 1
				else:
					y+=1
					direction += 1
					if direction == 4:
						direction = 0
			else:
				x-=1
				direction += 1
				if direction == 4:
					direction = 0
		elif direction == 2:
			x-=1
			if not (x < 0 or x == grid_size or y < 0 or y == grid_size):
				if get_grid(x,y) == 0:
					set_grid(x,y,value)
					value -= 1
				else:
					x+=1
					direction += 1
					if direction == 4:
						direction = 0
			else:
				x-=1
				direction += 1
				if direction == 4:
					direction = 0
		elif direction == 3:
			y+=1
			if not (x < 0 or x == grid_size or y < 0 or y == grid_size):
				if get_grid(x,y) == 0:
					set_grid(x,y,value)
					value -= 1
				else:
					y-=1
					direction += 1
					if direction == 4:
						direction = 0
			else:
				x-=1
				direction += 1
				if direction == 4:
					direction = 0
		if x < 0 or x == grid_size or y < 0 or y == grid_size:
			if x < 0:
				x = 0
			if y < 0:
				y = 0
			if x == grid_size:
				x = grid_size-1
			if y == grid_size:
				y = grid_size-1
			direction += 1
			if direction == 4:
				direction = 0

fill_grid(grid)

#print_grid()

def find_sum(g):
	dist = grid_size-1
	result = 0
	while dist >= 0:
		result += get_grid(grid_size-1-dist,grid_size-1-dist)
		result += get_grid(grid_size-1-dist,dist)
		dist -= 1
	if grid_size % 2 == 1:
		result -= 1
		pass
	print(result)

find_sum(grid)