def triangle(max = 100):
	n = 1
	while n < max:
		yield int(n*(n+1)/2)
		n+=1

def penta(max = 100):
	n = 1
	while n < max:
		yield int(n*(3*n-1)/2)
		n+=1

def hexa(max = 100):
	n = 1
	while n < max:
		yield int(n*(2*n-1))
		n+=1


triangles = []
pentas = []
hexas = []
limit = 150000
for i in triangle(limit):
	triangles.append(i)

for i in penta(limit):
	pentas.append(i)

for i in hexa(limit):
	hexas.append(i)

for i in triangles[50000:-1]:
	if i in pentas and i in hexas:
		print(i)