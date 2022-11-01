import random
import copy
import time
import os
import sys
import multiprocessing as mp

chars = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*.,?:; '\""]

class Word:
	def __init__(self, length):
		self.word = []
		self.fitness = length * len(chars)
		for i in range(length):
			self.word.append(random.choice(chars))

	def score(self,target):
		value = 0
		for i in range(len(target)):
			distance = abs(chars.index(target[i])-chars.index(self.word[i]))
			if (distance > round(len(chars)/2)):
			  distance = len(chars) - distance
			value+=distance
		self.fitness = value;
		return value

	def mutate(self,chance,intensity):
		for i in range(len(self.word)):
			if (random.randint(0,100) < chance*100):
				index = chars.index(self.word[i])
				index += random.choice((-intensity,-1,0,1,intensity))
				if index < 0:
					index = len(chars) - abs(index)
				if index > len(chars)-1:
					index = index - len(chars)
				self.word[i] = chars[index]
	def exchange(self,other):
		point = random.randint(1,len(self.word)-2)
		#mine = self.word[point:]
		theirs = other.word[point:]
		self.word = self.word[:point] + theirs
		#other.word = other.word[:point] + mine


class Population:
	def __init__(self,size,t,iters):
		self.population = []
		self.target = list(t)
		self.scores = []
		self.scorerange = 0
		self.elites = 2
		self.best = 0
		self.prevbest = 0
		self.staleness_factor = 0
		self.iters = iters
		for i in range(size):
			self.population.append(Word(len(self.target)))

	def print(self):
		for i in self.population:
			print("".join(i.word),i.score(self.target))



	def evaluate(self):
		self.scores = []
		for i in self.population:
			score = i.score(self.target)
		self.population.sort(key=lambda x: x.fitness)
		self.scorerange = (self.population[0].fitness,self.population[len(self.population)-1].fitness)
		self.prevbest = self.best
		self.best = self.population[0].fitness
		if self.best == self.prevbest:
			if self.staleness_factor < 0.9:
				self.staleness_factor += 0.005
		else:
			self.staleness_factor = 0
		#print("".join(self.population[0].word),self.scorerange, round(self.staleness_factor,3))
		self.reproduce()

	def reproduce(self):
		for i in range(self.elites,len(self.population)):
			self.population[i] = copy.deepcopy(self.population[random.randint(0,self.elites-1)])
		for i in range(self.elites,len(self.population)):
			self.population[i].exchange(self.population[random.randint(0,(self.elites-1) * 2)])
			self.population[i].mutate(0.05,1)

	def execute(self):
		self.evaluate()
		for i in range(self.iters):
			if i % 100 == 0:
				print("".join(self.population[0].word))
				sys.stdout.flush()
			if "".join(self.population[0].word) == "".join(self.target):
				return self.population[0].word
				
			self.evaluate()


def solve(string):
	cpus = os.cpu_count()
	A = Population(15,string,10000)
	return "".join(A.execute())




#print("".join(A.word))
if __name__ == '__main__':
	output = mp.Queue()
	processes = []

	string = """Jello Pudding is not very good, but I have learned to tolerate it.
	However, my favorite food is pizza, of the mushroom variety. This food has sated 
	my hunger many a time, and has long been a wonderful addition to any meal. And 
	thats great and all, but still man look at this genetic algorithm go boys, how 
	far we've come, holy shit. 
	"""
	#string = "Jello Pudding is not very good, but I have learned to tolerate it nonetheless."

	slist = list(string)
	leng = len(slist)
	width = round(leng / os.cpu_count())

	start_time = time.time()

	print("length of phrase:", len(string),", characters available:",len(chars), ", total search space:", len(chars) ** len(string) , "possiblilties.")
	# for i in range(os.cpu_count()):
	# 	piece = slist[i*width:i*width+width]
	# 	print("Starting a new process on core",i)
	# 	processes.append(mp.Process(target=solve(piece)))
	cpus = os.cpu_count()
	pool = mp.Pool(cpus)
	
	workers = [pool.apply_async(solve,args=(slist[i*width:i*width+width],)) for i in range(cpus)]


	


	# for process in processes:
	# 	process.start()

	# for process in processes:
	# 	process.join()

	results = [w.get() for w in workers]
	
	print("".join(results))

	print("Got it in", round((time.time() - start_time),3), "seconds")

