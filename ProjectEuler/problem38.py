def is_pandigital(n,start,stop):
	n_str = str(n)
	if len(n_str) > stop+1-start:
		return False
	for i in range(start,stop+1):
		if str(i) not in n_str:
			return False
	return True

#print(is_pandigital(124456789,1,9))
greatest = 0
for i in range(100000):
	result = str(i) 
	for k in range(2,11):
		result += str(i * k)
		if is_pandigital(int(result),1,9) and int(result) > greatest:
			print(int (result))
			greatest = int(result)

