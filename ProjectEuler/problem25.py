def generate_Fibonacci():
	a = 0
	b = 1
	while(True):
		c = a + b
		a = b
		b = c
		yield c

n = 1
for i in generate_Fibonacci():
	n_str = str(i)
	n+=1
	if len(n_str) >= 1000:
		print(i)
		print(n)
		break