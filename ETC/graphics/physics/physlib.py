from graphics import *
from math import sqrt, atan, cos, pi

class Vec2(Point):
	def __init__(self,a=0,b=0):
		self.x = a
		self.y = b

	def add(self,other):
		return Vec2(self.x + other.x,self.x + other.y)

	def sub(self,other):
		return Vec2(self.x - other.x,self.x - other.y)

	def mag(self):
		return abs(sqrt(self.x**2+self.y**2))

	def dir(self):
		if self.x > 0 and self.y > 0:
			return round(atan(self.y/(self.x+0.000000001)), 4)
		if self.x < 0 and self.y > 0:
			return round(atan(self.y/(self.x+0.000000001)) + pi, 4) 
		if self.x < 0 and self.y < 0:
			return round(atan(self.y/(self.x+0.000000001)) + (1.5*pi), 4) 
		if self.x > 0 and self.y < 0:
			return round(atan(self.y/(self.x+0.000000001)) + 2*pi, 4)
		if self.x == 0 and self.y == 0:
			return 0
		if self.x == 0:
			if self.y > 0:
				return round(pi/2,4)
			if self.y < 0:
				return round(1.5*pi,4)
		if self.y == 0:
			if self.x > 0:
				return 0
			if self.x < 0:
				return round(pi,4)

	def degree_dir(self):
		return round(self.dir() * 180 / pi,2)

	def normalize(self):
		return Vec2(round(self.x/(self.mag()+0.0001),4),round(self.y/(self.mag()+0.0001),4))

	def scalar_product(self,other):
		return round(self.mag() * other.mag() * cos(self.dir()-other.dir()),4)

	def scalar_mul(self,m):
		return Vec2(self.x*m,self.y*m)

	def Vec2_to_Point(self):
		return Point(self.x,self.y)

	def Point_to_Vec2(self,p):
		return Vec2(p.getX(),p.getY())

	def __repr__(self):
		return f"Vec2({self.x},{self.y})"
