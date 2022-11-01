summations = [[100]]

next_summations = []
for i in summations:
	remaining = i[0]
	for n in range(1,remaining//2):
		new_summation = i[:]
		new_summation[0] -= n
		new_summation += [n]
		next_summations += [new_summation]

summations = next_summations
print(summations)