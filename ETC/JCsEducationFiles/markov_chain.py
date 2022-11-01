from re import split
from random import randrange, choice
corpus = "".join(open("prideandprejudice.txt", "r").readlines())

words = split('[ :,\n_—-“”]',corpus)
words = [w.lower() for w in words if len(w) > 0]


dictionary = []
for i,word in enumerate(words):
	following_words = []
	if i < len(words)-1:
		following_words += [words[i+1]]
	for d in dictionary:
		if d[0] == word:
			d[1] += following_words
			break
	else:
		if len(following_words) > 0:
			dictionary += [[word, following_words]]
dictionary = sorted(dictionary)


def markov(l,d):
	output = ""
	index = randrange(len(d))
	for i in range(l):
		if len(d[index][1]) > 0:
			next_word = choice(d[index][1])
		else:
			next_word = choice(d[randrange(len(d))][1])
		if len(output) == 0:
			next_word = next_word.capitalize()
		if next_word == "i":
			next_word
		output += " " + next_word
		for n in d:
			if n[0] == next_word:
				index = d.index(n)
				break
		else:
			index = randrange(len(d))
		
	return output[1:] + "."

print(markov(250,dictionary))