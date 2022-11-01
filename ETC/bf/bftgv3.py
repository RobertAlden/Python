from math import sqrt
import sys

def factorize(i):
	f = [1]
	for k in range(2,i):
		if (i % k) == 0:
			f.append(k)
	return f

def lcd(factors):
	new_lcd = min(set.intersection(*map(set,factors[1:])))
	return new_lcd

def generate_char_map(s):
	chr_map = {c:[i for i, ltr in enumerate(s) if ltr == c] for c in s}
	return chr_map

def refine_char_map(cm, dist):
	new_char_map = {}
	keys = list(cm.keys())
	values = list(cm.values())

	print(keys)
	print(values)

	return new_char_map

def loopify(val,inner):
	string = ""
	if val == 1:
		return ">"+inner+"<"
	string += "".join(['+']*val) +'[>'
	string += inner
	string += '<-]'
	return string

def char_dist(s):
	last = ord(s[0])
	dists = []
	for i in s:
		dists += [ord(i) - last]
		last = ord(i)
	return dists

if len(sys.argv) < 2:
	raise Exception("Please provide input string with call.")
collapse_dist = 12
max_rep_chain = 10

verbose = False
if sys.argv[1] == "-v":
	verbose = True
	inp = sys.argv[2]
else:
	inp = sys.argv[1]
inp = [ord(x) for x in inp]


char_map = generate_char_map(inp)
raw_inp = inp[:]

inp = [k for k in char_map.keys()]

if verbose:
	print("Unmodifed ASCII:",raw_inp,"".join([chr(i) for i in raw_inp]))
	print("Character Map: ",char_map)
	print("Mapped String: ", "".join([chr(i) for i in inp]))

offset = [0] * len(inp)
for i in range(len(offset)):
	low = int(inp[i] / collapse_dist) * collapse_dist
	high = (int((inp[i]) / collapse_dist)+1) * collapse_dist
	if abs(inp[i] - low) <= abs(inp[i] - high):
		offset[i] = low - inp[i]
	else:
		offset[i] = high - inp[i]

raw_offset = [0] * len(raw_inp)
for i in range(len(raw_offset)):
	low = int(raw_inp[i] / collapse_dist) * collapse_dist
	high = (int((raw_inp[i]) / collapse_dist)+1) * collapse_dist
	if abs(raw_inp[i] - low) <= abs(raw_inp[i] - high):
		raw_offset[i] = low - raw_inp[i]
	else:
		raw_offset[i] = high - raw_inp[i]

for i in range(len(inp)):
	if ((inp[i]+offset[i]) % 2) != 0:
		offset[i] += 1

coll_inp = [inp[i]+offset[i] for i in range(len(inp))]
if verbose:
	print("Offset ASCII:",coll_inp,"".join([chr(i) for i in coll_inp]))
	print("Offsets:     ",offset)
	print("Raw Offsets: ",raw_offset)

raw_inp_char_dist = char_dist("".join([chr(i) for i in raw_inp]))

main_loops = factorize(collapse_dist)
outer_loops = []
while max(coll_inp) > max_rep_chain:
	for i in main_loops:
		for c in coll_inp:
			if c % i != 0:
				break
		else:
			coll_inp = [int(c/i) for c in coll_inp]
			outer_loops += [i]

inner_loops = [[max(factorize(i)),int(i/max(factorize(i)))] for i in coll_inp]
if verbose:
	print("Outer Loops: ",outer_loops)
	print("Inner Loops: ",inner_loops)
	print("Increments:  ",coll_inp)
	pass

start_flag = "->" 
reset = "+[-<+]-"

bf_out = ""


char_map_string = ">"
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

with open("out_bftgv3.bf",'w') as f:
	f.write(bf_out)
if verbose:
	print(bf_out)
	print("Program Length: ",len(bf_out))
print("generated: out_bftgv3.bf")