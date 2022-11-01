from graphics import *
import numpy as np
from time import perf_counter

scr_w,scr_h = 1600,1600
c_w, c_h = 4, 4
width, height = scr_w // c_w, scr_h // c_h
win = GraphWin("Game Of Life", scr_w, scr_h)
print(f"World Dimensions: {width=} {height=}")

grid = np.zeros((width,height),dtype=bool)
active_cells = []
changes = []
disp = []

for _y in range(height):
	row = []
	for _x in range(width):
		r = Rectangle(Point(_x*c_w,_y*c_h),Point(_x*c_w+c_w,_y*c_h+c_h))
		r.setFill("black")
		r.setWidth(0)
		row += [r]
	disp += [row]


def set_color(x,y,col):
	disp[y][x].setFill(col)


def toggle(x,y,mouse=False):
	global active_cells
	grid[y][x] = not grid[y][x]
	if grid[y][x]:
		disp[y][x].draw(win)
	else:
		disp[y][x].undraw()
	if mouse:
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
		

pause = True
while True:
	if not pause:
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
		print(f"Time: {round(end - start,4)} seconds.")
	else:
		mouseInput = win.checkMouse()
		if mouseInput != None:
			m_x = int(mouseInput.getX() // c_w)
			m_y = int(mouseInput.getY() // c_h)
			toggle(m_x,m_y,mouse=True)

	inp = win.checkKey()
	if inp != "":
		if inp == "q":
			win.close()
			break
		if inp == " ":
			pass
		if inp == "f":
			pause = not pause
			print("Paused:",pause)
