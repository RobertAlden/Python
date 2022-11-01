from math import sqrt
from re import fullmatch

for i in range(1010101010,1389026624):
	num = str(i * i)
	#print(num)
	if fullmatch(r'1[0-9]2[0-9]3[0-9]4[0-9]5[0-9]6[0-9]7[0-9]8[0-9]9[0-9]0',num):
		print(i)
		break