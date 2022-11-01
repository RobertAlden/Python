


def num_to_text(n,d):
	if d == 0:
		text = {
			0: "",
			1: "one",
			2: "two",
			3: "three",
			4: "four",
			5: "five",
			6: "six",
			7: "seven",
			8: "eight",
			9: "nine"
		}
		return text.get(n)
	if d == -1:
		text = {
			0: "",
			1: "eleven",
			2: "twelve",
			3: "thirteen",
			4: "fourteen",
			5: "fifteen",
			6: "sixteen",
			7: "seventeen",
			8: "eighteen",
			9: "nineteen"
		}
		return text.get(n)
	if d == 1:
		text = {
			0: "",
			1: "ten",
			2: "twenty",
			3: "thirty",
			4: "forty",
			5: "fifty",
			6: "sixty",
			7: "seventy",
			8: "eighty",
			9: "ninety"
		}
		return text.get(n)

def print_number_text(n):
	phrase = []
	chars = list(str(n))
	#print(chars)
	chars.reverse()
	
	for i in range(len(chars)):
		k = i % 3
		div = i // 3
		if div > 0 and k == 0 and chars[i] != "0":
			phrase.append(" ")
			numerals = {
				1: "thousand",
				2: "million",
				3: "billion",
				4: "trillion",
				5: "quadrillion",
				6: "quintillion",
				7: "sextillion",
				8: "septillion",
				9: "octillion",
				10: "nonillion",
				11: "decillion",
				12: "undecillion",
				13: "duodecillion",
				14: "tredecillion",
				15: "quattuordecillion",
				16: "quindecillion",
				17: "sexdecillion",
				18: "septendecillion",
				19: "octodecillion",
				20: "novemdecillion",
				21: "vigintillion"
			}
			phrase.append(numerals.get(div))
			phrase.append(" ")
		if k == 0:
			if len(chars) > i+1 and chars[i+1] == "1":
				phrase.append(num_to_text(int(chars[i]),-1))
			else:
				phrase.append(num_to_text(int(chars[i]),0))
		elif k == 1:
			phrase.append(" ")
			if chars[i] != "1":
				phrase.append(num_to_text(int(chars[i]),1))
			elif chars[i-1] == "0":
				phrase.append(num_to_text(int(chars[i]),1))

		elif k == 2 and chars[i] != "0":
			if chars[i-1] != "0" or chars[i-2] != "0":
				phrase.append(" and ")
			phrase.append(" hundred")
			phrase.append(num_to_text(int(chars[i]),0))

	phrase.reverse()
	return "".join(phrase)




numbers = []

for i in range(1,1001):
	print(i,print_number_text(i))
	numbers.append(print_number_text(i))

g_number = " ".join(numbers)
g_number = "".join(g_number.split())
print(g_number)
print(len(g_number))

print(print_number_text(23439874619857401237850178205701334045))