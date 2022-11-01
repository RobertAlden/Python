limit = 1000000
numbers = [1] * (limit+1)
numbers[0] = 0
numbers[1] = 0

for x,t in enumerate(numbers):
	if t:
		for k in range(x+x,limit+1,x):
			numbers[k] = 0

primes = [i for i,x in enumerate(numbers) if x if i > 100000]
org_primes = []
for k in range(1,len(str(limit))):
	p0 = [i for i in primes if list(str(i)).count('0') == k]
	p1 = [i for i in primes if list(str(i)).count('1') == k]
	p2 = [i for i in primes if list(str(i)).count('2') == k]
	m = list(set(p0+p1+p2))
	print(len(m),k)
	org_primes.extend(m)

org_primes = sorted(list(set(org_primes)))
#print(org_primes,len(org_primes))

def create_p_group(n):
	groups = []
	d_filters = []
	filter0 = []
	filter1 = []
	filter2 = []
	for i in str(n):
		filter0.append(str(int(i == '0')))
		filter1.append(str(int(i == '1')))
		filter2.append(str(int(i == '2')))
	d_filters.append("".join(filter0))
	d_filters.append("".join(filter1))
	d_filters.append("".join(filter2))
	for d_filter in d_filters:
		group = []
		s = list(str(n))
		for k in range(10):
			for i,x in enumerate(d_filter):
				if int(x) and i in range(len(s)):
					s[i] = str(k)
			p = int("".join(s))
			if p in primes and p not in group:
				group.append(p)
		groups.append(group)

	len_g = [len(x) for x in groups]
	l = len_g.index(max(len_g))

	return groups[l]



for P in org_primes:
	print(P)
	g = create_p_group(P)
	if len(g) > 7:
		print(g)
		break
