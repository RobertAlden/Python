from random import randint


size = 10
data_size = 1000
data = [randint(int("".join(["1"]+["0"]*(size-1))),int("".join(["9"]+["9"]*(size-1)))) for x in range(data_size)]
#data_sort = sorted(data[:])
#print(data_sort)
index = [0]*10
for i in range(size):
	sorted_data = [0]*data_size
	for n in data:
		str_n = str(n)
		digit = int(str_n[-(i+1)])
		index[digit] += 1
	for k in range(len(index)-1):
		index[k+1] += index[k] #Prefix sum
	for b in reversed(data):
		digit = int(str(b)[-(i+1)])
		sorted_data[index[digit]-1] = b
		index[digit] -= 1
	data = sorted_data[:]
	index = [0]*10
print(data)