coins = [0,0,0,0,0,0,0,1]
divisions = [1,2,5,10,20,50,100,200]

def makeChange(coinage,iters):
	iters += 1
	for i in range(len(coinage)-1,0,-1):
		if coinage[i] > 0:
			value = divisions[i]
			new_coins = value // divisions[i-1]
			if new_coins * divisions[i-1] < value:
				coinage[i-2] += 1

			coinage[i] -= 1
			coinage[i-1] += new_coins
			break

	print(coinage)
	if coinage[0] != 200:
		makeChange(coinage,iters)
	else:
		print(iters)


makeChange(coins,1)