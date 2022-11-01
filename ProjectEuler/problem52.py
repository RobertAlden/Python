def contains_digits(a,b):
	d_a = sorted(list(str(a)))
	d_b = sorted(list(str(b)))
	return d_a == d_b



for i in range(10,1000000):
	for k in range(2,7):
		if not contains_digits(i,k*i):
			break
	else:
		print(i)
		for k in range(2,7):
			print(i*k)
		break