from graphics import *
from physlib import *
from random import random

scr_w,scr_h = 1024,1024
c_w, c_h = 16, 16
width, height = scr_w // c_w, scr_h // c_h
win = GraphWin("Physics", scr_w, scr_h, autoflush=False)
grid = []
for y in range(height):
	grid += [[Vec2((random()-.5)*5,(random()-.5)*5) for x in range(width)]]

num_of_circles = 10


def main():
	circles = []

	for i in range(num_of_circles):
		a = Vec2(random()*scr_w,random()*scr_h)
		c = Circle(a,5)
		v = Vec2(0,0)
		c.draw(win)
		circles += [[c,v]]

	while(True):
		for c in circles:
			gx = (int(c[0].getCenter().getX() // c_w)+width) % width
			gy = (int(c[0].getCenter().getY() // c_h)+height) % height
			
			gvec = grid[gy][gx]
			c[1] = c[1].add(gvec)
			c[1] = c[1].scalar_mul(.98)
			c[0].move(c[1].x,c[1].y)
		update(30)
	win.getMouse()

	win.close()


if __name__ == '__main__':
	main()