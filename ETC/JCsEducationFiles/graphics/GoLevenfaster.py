from graphics import *
import numpy as np
import ctypes
from multiprocessing import Pool, RawArray
from time import perf_counter
from functools import partial

scr_w,scr_h = 1600,1600
c_w, c_h = 32, 32
width, height = scr_w // c_w, scr_h // c_h
var_dict = {}

def set_color(x,y,col):
	disp[y][x].setFill(col)


def toggle(i,mouse=False):
	global active_cells, sharedArray
	x = i % width
	y = i // width
	sharedArray[i] = not sharedArray[i]
	if sharedArray[i]:
		disp[y][x].draw(win)
	else:
		disp[y][x].undraw()
	if mouse:
		for i in range(-1,2):
			for k in range(-1,2):
				l = (y+k) * width + (x+i)
				if l not in active_cells:
					active_cells += [l]

def vec_init(x):
	global var_dict
	var_dict['X'] = x

def vectorized_process(i):
	a = var_dict['X']
	cx = i % width
	cy = i // width

	neighbors = 0
	for _y in range(-1,2):
		for _x in range(-1,2):
			if _x != 0 or _y != 0:
				neighbors += a[(cy+_y)*width+(cx+_x)]

	if a[cy*width+cx]:
		if neighbors != 2 and neighbors != 3:
			return cy*width+cx
	else:
		if neighbors == 3:
			return cy*width+cx


def main():
	global grid,disp,win,active_cells,changes,sharedArray
	win = GraphWin("Game Of Life", scr_w, scr_h)
	print(f"World Dimensions: {width=} {height=}")

	grid = np.zeros(width*height,dtype=bool)
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

	#manager = Manager()
	Ashape = (width,height) 
	sharedArray = RawArray('b', width*height)
	#sharedArray_np = np.frombuffer(sharedArray, dtype=bool).reshape(X_shape)

	pause = True
	while True:
		if not pause:
			start = perf_counter()
			print(len(active_cells))

			#flat_grid = grid.reshape(width*height, order='C')
			#active_cells = [a[1] * width + a[0] for a in active_cells]

			
			with Pool(processes=4, initializer=vec_init, initargs=(sharedArray,)) as p:
					#result = pool.map(worker_func, range(X_shape[0]))
					changes = p.map(vectorized_process, active_cells)
			#qqprint(changes)
			changes = [c for c in changes if c is not None]
			active_cells = []
			for c in changes:
				toggle(c)
				c_x = c % width
				c_y = c // width
				for i in range(-1,2):
					for k in range(-1,2):
						l = (c_y+k) * width + (c_x+i)
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
				m_i = m_y * width + m_x
				toggle(m_i,mouse=True)
				#print(m_x,m_y,grid[m_y,m_x])

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


if __name__ == '__main__':
	main()

