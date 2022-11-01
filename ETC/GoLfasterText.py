import numpy as np
from time import sleep,perf_counter
from random import random

width, height = 20, 20
active_cells = []
changes = []


def disp():
	chars = ["  ","[]"]
	for i in range(height):
		print("".join([chars[int(n)] for n in grid[i]]))
	sleep(1/30)


def toggle(x,y,init=False):
	global active_cells
	grid[y][x] = not grid[y][x]
	if init:
		for i in range(-1,2):
			for k in range(-1,2):
				l = [(x+i)%width,(y+k)%height]
				if l not in active_cells:
					active_cells += [l]
	

def process_cell(cx,cy):
	global changes,grid
	off_x = 0
	off_y = 0

	if cx == 0:
		grid = np.roll(grid,1,axis=1)
		off_x += 1
	if cx == width-1:
		grid = np.roll(grid,-1,axis=1)
		off_x -= 1
	if cy == 0:
		grid = np.roll(grid,1,axis=0)
		off_y += 1
	if cy == width-1:
		grid = np.roll(grid,-1,axis=0)
		off_y -= 1

	cx += off_x
	cy += off_y

	neighbors = np.sum(grid[cy-1:cy+2,cx-1:cx+2]) - grid[cy,cx]
	if grid[cy,cx]:
		if neighbors != 2 and neighbors != 3:
			changes += [[(cx-off_x),(cy-off_y)]]
	else:
		if neighbors == 3:
			changes += [[(cx-off_x),(cy-off_y)]]

	cx -= off_x
	cy -= off_y

	if cx == 0:
		grid = np.roll(grid,-1,axis=1)
	if cx == width-1:
		grid = np.roll(grid,1,axis=1)
	if cy == 0:
		grid = np.roll(grid,-1,axis=0)
	if cy == width-1:
		grid = np.roll(grid,1,axis=0)

		
try:
	initial = "".join(open("gol_init.txt", "r").readlines())
	initial = initial.split()
	iters = int(initial[0])
	initial = initial[1:]
	print(iters)
	print("Loading Successful")
except FileNotFoundError:
	initial = None
	iters = 0

grid = np.zeros((width,height),dtype=bool)
if initial != None:
	for y in range(height):
		for x in range(width):
			try:
				if initial[y][x] == "O":
					toggle(x,y,init=True)
			except IndexError:
				pass
else:
	grid = np.zeros((width,height),dtype=bool)

print(f"World Dimensions: {width=} {height=}")

for _i in range(iters):
	start = perf_counter()
	if len(active_cells) == 0:
		for _y in range(height):
			for _x in range(width):
				process_cell(_x,_y)
	else:
		for a in active_cells:
			process_cell(a[0],a[1])
	active_cells = []
	for c in changes:
		toggle(c[0],c[1])
		for i in range(-1,2):
			for k in range(-1,2):
				l = [(c[0]+i)%width,(c[1]+k)%height]
				if l not in active_cells:
					active_cells += [l]
	changes = []
	end = perf_counter()
	disp()
	disp_time = perf_counter()
	print("---------------")
	print(f"Frame {_i+1} Compute Time: {round(end - start,5)} seconds.")
	print(f"Frame {_i+1}    Disp Time: {round(disp_time - end,5)} seconds.")
	print("---------------")
	
	