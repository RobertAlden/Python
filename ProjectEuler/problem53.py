from math import factorial

def combinatoric_selections(n,r):
    return round(factorial(n) / (factorial(r) * factorial(n - r)))

amount = 0

for i in range(2,101):
    for k in range(2,i+1):
        result = combinatoric_selections(i,k)
        if result > 1000000:
            amount += 1
        print(f"{i} {k} {result}")

print(amount)