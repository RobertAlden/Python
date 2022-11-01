limit =  10001

def lychrel(a):
	num = [str(i) for i in str(a)]
	rev = list(num)
	rev.reverse()
	num = int("".join(num))
	rev = int("".join(rev))
	#print(num,rev,num + rev)
	return num + rev

def is_palidrome(a):
	num = [str(i) for i in str(a)]
	rev = list(num)
	rev.reverse()
	return rev == num

def test(a):
	count = 0
	number = a
	while count <= 50:
		if is_palidrome(number):
			break
		else:
			number = lychrel(number)
			count+=1
	print(a,count)
	return count > 50

test(196)

total = 0
for i in range(0, limit):
	total += test(i)

print(total)