largest = 0

for a in range(999,100,-1):
	for b in range(999,100,-1):
		value = a*b
		lst = [int(i) for i in str(value)]
		head = 0;
		tail = len(lst)-1
		#print(a,"*",b,"=",a*b)
		palindrome = 1
		for i in range(0,round(len(lst)/2)):
			if lst[head] == lst[tail]:
				head+=1
				tail-=1
			else:
				palindrome = 0
				break
		if palindrome == 1:
			if a*b > largest:
				largest = a*b
print(largest)
