from graphics import *
from physlib import *

scr_w,scr_h = 1024,1024
c_w, c_h = 16, 16
width, height = scr_w // c_w, scr_h // c_h
win = GraphWin("Physics", scr_w, scr_h)

grid = []
buffer = []
disp = []
for _y in range(height):
	grid += [[0] * width]
	buffer += [[0] * width]
	row = []
	for _x in range(width):
		r = Rectangle(Point(_x*c_w,_y*c_h),Point(_x*c_w+c_w,_y*c_h+c_h))
		r.setFill("white")
		r.draw(win)
		row += [r]
	disp += [row]

def set_color(x,y,col):
	disp[y][x].setFill(col)

def toggle(x,y,set_flag=-1):
	if set_flag != -1:
		grid[y][x] = set_flags
	else:	
		grid[y][x] = not grid[y][x]

	if grid[y][x]:
		set_color(x,y,"black")
	else:
		set_color(x,y,"white")

pause = True
while True:
	mouseInput = win.checkMouse()
	if mouseInput != None:
		print(mouseInput, width, height)
		m_x = int(mouseInput.getX() // c_w)
		m_y = int(mouseInput.getY() // c_h)
		print(m_x,m_y)
		toggle(m_x,m_y)

	if not pause:
		for _y in range(1,height-1):
			for _x in range(1,width-1):
				neighbors = 0
				for i in range(-1,2):
					for k in range(-1,2):
						neighbors += grid[_y+i][_x+k]
				if grid[_y][_x]:
					neighbors -= 1
					if neighbors == 2 or neighbors == 3:
						buffer[_y][_x] = 1
						set_color(_x,_y,"black")
					else:
						buffer[_y][_x] = 0
						set_color(_x,_y,"white")
				else:
					if neighbors == 3:
						buffer[_y][_x] = 1
						set_color(_x,_y,"black")
					else:
						buffer[_y][_x] = 0
						set_color(_x,_y,"white")
		grid, buffer = buffer, grid
		buffer = [[0]*width for _i in range(height)]

	inp = win.checkKey()
	if inp != "":
		if inp == "q":
			win.close()
			break
		if inp == "f":
			pause = not pause
			print("Paused:",pause)
