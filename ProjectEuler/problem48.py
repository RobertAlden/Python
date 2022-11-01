n = 0
total = 0
while n < 1000:
	n+=1
	total += n**n

print(total % 10000000000)