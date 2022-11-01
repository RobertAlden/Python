from re import split
from random import randrange, choice
corpus = "".join(open("corpus.txt", "r").readlines())

words = split('[ ,:;\t\s\-—\"]',corpus)
words = [w.lower() for w in words if len(w) > 0]
for i,word in enumerate(words):
	if word[-1] == "." and word != ".":
		print(word,i)
		words.pop(i)
		words.insert(i,word[:-1])
		words.insert(i+1,".")


dictionary = []
count = 0
for i,word in enumerate(words):
	following_words = []
	if word == ".":
		count = 0
	if i < len(words)-1:
		following_words += [[words[i+1],count]]
	for d in dictionary:
		if d[0] == word:
			d[1] += following_words
			break
	else:
		if len(following_words) > 0:
			dictionary += [[word, following_words]]
	count += 1
#print(words)
dictionary = sorted(dictionary)
for d in dictionary:
	d[1] = [e for e in d[1] if e != "."]
	print(d[0],d[1])



def markov(l,c,d):
	for d in dictionary:
		if len(d[1]) > 0:
			try:
				d[1][0][1] = d[1][0][1]/c
			except IndexError:
				print(d[1][0][1],"ERROR")
				
	output = ""
	index = randrange(len(d))
	count = 0
	running_count = 0
	error_margin = 0
	for i in range(l):
		while True:
			if len(d[index][1]) > 0:
				next_word = choice(d[index][1])
				print(next_word)

				next_word = choice(d[index][1])
			else:
				next_word = choice(d[randrange(len(d))][1])
				count = next_word[1]
				next_word = choice(d[randrange(len(d))][1])[0]

			if running_count - count <= error_margin:
				error_margin = 0
				break
			error_margin+=1

		running_count += 1
		if running_count == c+1:
			running_count = 0
			next_word = "."

		if len(output) == 0 or next_word == "i" or output[-1] == ".":
			next_word = next_word.capitalize()

		if next_word == ".":
			output += next_word
		else:
			output += " " + next_word

		
		for n in d:
			if n[0] == next_word:
				index = d.index(n)
				break
		else:
			index = randrange(len(d))
		
	return output[1:] + "."

print(markov(250,5,dictionary))