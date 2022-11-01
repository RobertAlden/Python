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


for l in range(limit-1):
	p3 = numbers[2][l] 
	if p3 > 1000 and p3 < 10000:
		n4 = [i for i in numbers[4] if (str(i)[:2] == str(p3)[2:]) and len(str(i)) == 4]
		for p4 in n4:
			print(n4)
			n5 = [i for i in numbers[5] if (str(i)[:2] == str(p4)[2:]) and len(str(i)) == 4]
			for p5 in n5:
				print(n5)
				n6 = [i for i in numbers[6] if (str(i)[:2] == str(p5)[2:]) and len(str(i)) == 4]
				for p6 in n6:
					print(n6)
					n7 = [i for i in numbers[7] if (str(i)[:2] == str(p6)[2:]) and len(str(i)) == 4]
					for p7 in n7:
						print(n7)
						n8 = [i for i in numbers[8] if (str(i)[:2] == str(p7)[2:]) and len(str(i)) == 4]
						for p8 in n8:
						 	if str(p8)[2:] == str(p3)[:2]:
						 		
						 		print(p8)
								
								
