multiples = []
s = 0

for i in range(0,1000):
	if (i % 3 == 0 or i % 5 == 0) and i not in multiples:
		multiples.append(i)


s = sum(multiples)
print(multiples , s)


def sumn(d, n):
	n //= d
	return d * n * (n + 1) / 2


print(sumn(3,1000-1)+sumn(5,1000-1)-sumn(15,1000-1))