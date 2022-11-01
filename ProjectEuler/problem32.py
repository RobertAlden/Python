def is_pandigital(n,start,stop):
	n_str = str(n)
	if len(n_str) > stop+1-start:
		return False
	for i in range(start,stop+1):
		if str(i) not in n_str:
			return False
	return True


total = 0
limit = 3000
previous = list()
for i in range(limit):
	for k in range(limit):
		product = i * k
		n_str = str(i) + str(k) + str(product)
		if is_pandigital(n_str,1,9) and product not in previous:
			previous.append(product)
			total += product
print(previous)
print(total)