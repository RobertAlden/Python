from re import split
from random import randrange, choice
corpus = "".join(open("corpus.txt", "r").readlines())

delimiters = '[:,\n—]'
words = split('[ \W]',corpus)
words = [w.lower() for w in words if len(w) > 0]

print(words)

dictionary = []
count = 0
for i,word in enumerate(words):
	following_words = []
	if word in delimiters:
		print(word)
		count = 0
	else:
		count += 1
		if i < len(words)-1:
			following_words += [(words[i+1],count+1)]

		for d in dictionary:
			if d[0] == word:
				d[1] += following_words
				break
		else:
			if len(following_words) > 0:
				dictionary += [[word, following_words]]
	
#print(words)
dictionary = sorted(dictionary)
for d in dictionary:
 	print(d[0],d[1])



def markov(l,d):
	output = ""
	index = randrange(len(d))
	for i in range(l):
		if len(d[index][1]) > 0:
			next_word = choice(d[index][1])[0]
		else:
			next_word = choice(d[randrange(len(d))][1])[0]
		if len(output) == 0:
			next_word = next_word.capitalize()
		if next_word == "i": 
			next_word = next_word.capitalize()
		output += " " + next_word
		for n in d:
			if n[0] == next_word:
				index = d.index(n)
				break
		else:
			index = randrange(len(d))
		
	return output[1:] + "."

print(markov(100,dictionary))