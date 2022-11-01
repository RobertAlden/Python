from graphics import *
from math import sqrt, inf, factorial
from random import random, shuffle, randint
from time import perf_counter

scr_w,scr_h = 1024,1024

win = GraphWin("Game Of Life", scr_w, scr_h)

number_of_cities = 20
search_space = factorial(number_of_cities)
print(search_space)
cities = []

pop_size = 100
population = []
fitness = [0]*pop_size
mutation_rate = .5
max_mutation = .99
min_mutation = .1


def dist(p1,p2):
	return sqrt(((p2.getX() - p1.getX())**2) + (p2.getY() - p1.getY())**2)


for i in range(number_of_cities):
	x,y = int(random()*scr_w),int(random()*scr_h)
	c = Circle(Point(x,y),10)
	c.setFill(color_rgb(x*21%255,y*23%255,i*25%255))
	c.draw(win)
	cities += [[x,y]]


base = [i for i in range(number_of_cities)]
shuffle(base)
population = []
for i in range(pop_size):
	inst = base[:]
	shuffle(inst)
	population += [inst]

best = None
count = 0
best_fitness = inf
path = Polygon([Point(cities[i][0],cities[i][1]) for i in base])
while True:
	if best != None:
		path.draw(win)
		best_indivs = best
		population = []
		population += best_indivs
		for i in range(pop_size-len(best)):
			inst = best_indivs[int(random()*len(best_indivs))][:]
			if random() <= mutation_rate:
				for i in range(randint(1,100)):
					a_i = randint(0,len(inst)-1)
					b_i = randint(0,len(inst)-1)
					while b_i == a_i:
						b_i = randint(0,len(inst)-1)

					a = inst[a_i]
					b = inst[b_i]
					inst[a_i] = b
					inst[b_i] = a

			population += [inst]
	for i,p in enumerate(population):
		d = 0
		for k in range(len(p)-1):
			px1 = cities[p[k]][0]
			py1 = cities[p[k]][1]
			
			px2 = cities[p[k+1]][0]
			py2 = cities[p[k+1]][1]
			
			d+=dist(Point(px1,py1),Point(px2,py2))
		d+= dist(Point(cities[p[-1]][0],cities[p[-1]][1]),Point(cities[p[0]][0],cities[p[0]][1]))
		fitness[i] = (int(d),i)

	fitness = sorted(fitness,key=lambda x:x[0])
	elites = int(pop_size * 0.1)+1
	best = [population[fitness[n][1]] for n in range(elites)]
	best += [population[fitness[-(n+1)][1]] for n in range(elites)]
	

	if fitness[0][0] < best_fitness:
		best_fitness = fitness[0][0]
		mutation_rate = min_mutation
	else:
		mutation_rate += 0.01
		if mutation_rate > max_mutation:
			mutation_rate = max_mutation
	path.undraw()
	path = Polygon([Point(cities[i][0],cities[i][1]) for i in best[0]])
	count+=1
	print(fitness[0][0],round(mutation_rate,3),count/search_space)

win.close()