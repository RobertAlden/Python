def p3(n):
	return n*(n+1)//2

def p4(n):
	return n**2

def p5(n):
	return n*(3*n-1)//2

def p6(n):
	return n*(2*n-1)

def p7(n):
	return n*(5*n-3)//2

def p8(n):
	return n*(3*n-2) 	

numbers = [[0],[0]]
limit = 142 # ensures p3(limit) > 9999
for i in range(3,9):
	numbers += [eval("[p"+str(i)+"(n) for n in range(1,"+str(limit)+")]")]


