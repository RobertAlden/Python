def CharDist(s):
	last = ord(s[0])
	dists = []
	for i in s:
		dists += [last - ord(i)]
		last = ord(i)
	return dists

print(CharDist("Hello World!"))