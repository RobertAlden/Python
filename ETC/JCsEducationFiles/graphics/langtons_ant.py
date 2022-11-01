from graphics import *


scr_w,scr_h = 1600,1600
c_w, c_h = 16, 16
width, height = scr_w // c_w, scr_h // c_h
win = GraphWin("Langton's Ant", scr_w, scr_h)

grid = []
disp = []
for _y in range(height):
	grid += [[0] * width]
	row = []
	for _x in range(width):
		r = Rectangle(Point(_x*c_w,_y*c_h),Point(_x*c_w+c_w,_y*c_h+c_h))
		r.setFill("white")
		r.draw(win)
		row += [r]
	disp += [row]

def set_color(x,y,col):
	disp[y][x].setFill(col)

l_x, l_y = width // 2, height // 2
 

direction = 0
rules = [[1,"red"],[-1,"blue"],[-1,"grey"],[1,"white"]]
iterations = 16000

for i in range(iterations):
	rule = rules[grid[l_y][l_x]]
	direction += rule[0]
	set_color(l_x,l_y,rule[1])
	grid[l_y][l_x] = (grid[l_y][l_x] + 1) % len(rules)
	
	direction %= 4
	if direction == 0:
		l_y -= 1
	if direction == 1:
		l_x += 1
	if direction == 2:
		l_y += 1
	if direction == 3:
		l_x -= 1

	
win.getMouse()
win.close()