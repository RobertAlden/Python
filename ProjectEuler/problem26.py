def cycle_count(n):
	vals = []
	rem = 1 % n
	vals.append(rem)
	while True:
		rem *= 10
		rem = rem % n
		if rem not in vals:
			vals.append(rem)
		else:
			break
	return len(vals)

highest = 0
x = 0
for i in range(2,1000):
	m = cycle_count(i) 
	if m > highest:
		highest = m
		x = i

print("1/" + str(x),highest)