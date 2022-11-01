from math import sqrt
import sys


if len(sys.argv) < 2:
	raise Exception("Please provide input string with call.")

collapse_dist = 12
max_rep_chain = 10

inp = sys.argv[1]
inp = [ord(x) for x in inp]

char_map = {c:[i for i, ltr in enumerate(inp) if ltr == c] for c in inp}
print("Character Map: ",char_map)
raw_inp = inp[:]
inp = [k for k in char_map.keys()]
print("Char Mapped String: ", inp)

offset = [0] * len(inp)
for i in range(len(offset)):
	low = int(inp[i] / collapse_dist) * collapse_dist
	high = (int((inp[i]) / collapse_dist)+1) * collapse_dist
	if abs(inp[i] - low) <= abs(inp[i] - high):
		offset[i] = low - inp[i]
	else:
		offset[i] = high - inp[i]

for i in range(len(inp)):
	if ((inp[i]+offset[i]) % 2) != 0:
		offset[i] += 1

print("Input ASCII:",inp,"".join([chr(i) for i in inp]))
coll_inp = [inp[i]+offset[i] for i in range(len(inp))]
print("Offset ASCII:",coll_inp,"".join([chr(i) for i in coll_inp]))
print("Offsets:",offset)

def factorize(i):
	f = [1]
	for k in range(2,i):
		if (i % k) == 0:
			f.append(k)
	return f

def lcd(factors):
	new_lcd = min(set.intersection(*map(set,factors[1:])))
	return new_lcd

main_loops = factorize(collapse_dist)
outer_loops = []
print(main_loops)
while max(coll_inp) > max_rep_chain:
	for i in main_loops:
		for c in coll_inp:
			if c % i != 0:
				break
		else:
			coll_inp = [int(c/i) for c in coll_inp]
			outer_loops += [i]
			#print(i,coll_inp)

print(coll_inp)
final_loops = [[max(factorize(i)),int(i/max(factorize(i)))] for i in coll_inp]
print(final_loops)

# produce loops
def loopify(string,val,inner):
	string += "".join(['+']*val) +'[>'
	string += inner
	string += '<-]'
	return string

bf_out = ""

for i in final_loops:
	bf_out = loopify(bf_out,i[0],"".join(['+']*i[1]))
	bf_out += ">>"
bf_out += "".join(['<<']*(len(inp)))


inside = bf_out[:]
bf_out = ""

for i in outer_loops:
	bf_out = loopify("",i,inside)
	inside = bf_out[:]
bf_out += "<"
bf_out += "".join(['>>']*(len(outer_loops)-1))

print(bf_out.count(">") - bf_out.count("<"))

offset_string = "<"
for i in offset:
	if i < 0:
		offset_string += "".join(['+']*abs(i))
	elif i > 0:
		offset_string += "".join(['-']*abs(i))
	offset_string += ">>"

bf_out += offset_string
bf_out += "<" * (len(inp) * 2)

print(bf_out.count(">") - bf_out.count("<"))


char_map_string = ""
curr_char_offset = 0
target_offset = 0
direction = 1
for i in range(len(raw_inp)):
	for o,v in enumerate(char_map.values()):
		if i in v:
			target_offset = abs(o-curr_char_offset)
			direction = ((o-curr_char_offset) > 0)
			break
	for m in range(target_offset):
		if direction:
			char_map_string += ">>"		
		else:
			char_map_string += "<<"
	curr_char_offset += (o-curr_char_offset)
	char_map_string += "."

bf_out += char_map_string
with open("out_bftgv1.bf",'w') as f:
	f.write(bf_out)

print(bf_out)
print("Program Length: ",len(bf_out))