import math

def gen_triplets(n):
	trips = []
	for a in range(1,n//3):
		for b in range(1,n//2):
			#if i**2 + k**2 == (n-(i+k))**2:
			c = n - a - b
			if a**2 + b**2 == c**2 and (a,b,c) not in trips:
				trips.append((a,b,c))
	return trips
			
finals = [0] * 1001

for i in range(1001):
	finals[i] = len(gen_triplets(i))
	print(i,finals[i])


print(finals,max(finals),finals.index(max(finals)))