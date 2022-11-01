import math

for a in range(1000):
	for b in range(1000):
		c = math.sqrt(a**2+b**2)
		if c == int(c) and a < b < c:
			c = int(c)
			if a+b+c == 1000:
				print(a,b,c,a+b+c,a*b*c)