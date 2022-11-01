power = 5
maxval = 10000000

final_total = 0
for n in range(2,maxval):
	n_total = 0
	n_str = str(n)
	for char in range(len(n_str)):
		number = int(n_str[char])
		n_total += number**power
		if n_total > n:
			break
	if n_total == n:
		final_total+=n_total
		print(n_total)
print(final_total)

