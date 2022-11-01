limit = 1000000
#search = 1000000
search = 1000000
start = '0'
for i in range(1,limit+1):
	start += str(i)

begin = 1
result = 1
while begin <= search:
	if begin < len(start):
		print(start[begin])
		result *= int(start[begin])
		begin *= 10
	else:
		break

#print(start)
print(result)