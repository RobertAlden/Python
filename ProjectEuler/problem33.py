digits = [1,2,3,4,5,6,7,8,9]

def join_n(a,b):
	return int(str(a) + str(b))

desired_fractions = []

for numer in digits:
	for denom in digits:
		if numer < denom:
			fraction = numer/denom
			for cancel in digits:
				tests = []
				tests.append(join_n(numer,cancel)/join_n(denom,cancel))
				tests.append(join_n(cancel,numer)/join_n(cancel,denom))
				tests.append(join_n(cancel,numer)/join_n(denom,cancel))
				tests.append(join_n(numer,cancel)/join_n(cancel,denom))

				if fraction in tests:
					i = tests.index(fraction)
					d = {
						0:(numer,cancel,denom,cancel),
						1:(cancel,numer,cancel,denom),
						2:(cancel,numer,denom,cancel),
						3:(numer,cancel,cancel,denom)
					}
					res = d.get(i)
					desired_fractions.append((res,fraction))


print(desired_fractions)
print(1/4 * 1/5 * 2/5 * 1/2)