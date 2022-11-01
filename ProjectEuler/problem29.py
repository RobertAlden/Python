max_exponent = 100
max_base = 100

results = list()

for b in range(2,max_base+1):
	for e in range(2,max_exponent+1):
		value = b**e
		if value not in results:
			results.append(value)

print(results)
print(len(results))

