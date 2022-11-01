from graphics import *


scr_w,scr_h = 1024,1024
c_w, c_h = 32, 32
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

#set_color(5,5,"red")

l_x, l_y = width // 2, height // 2
 

direction = 0
rules = [[0,1,1,"white"],[1,-1,0,"red"]]
iterations = 1000

for i in range(iterations):
	if direction == 0:
		l_y -= 1
	if direction == 1:
		l_x += 1
	if direction == 2:
		l_y += 1
	if direction == 3:
		l_x -= 1
	if direction == 4:
		direction = 0
		l_y -= 1

	print(l_x,l_y,direction)
	for r in rules:
		if grid[l_y][l_x] == r[0]:
			direction += r[1]
			grid[l_y][l_x] = r[2]
			set_color(l_x,l_y,r[3])
			break

win.getMouse()




win.close()