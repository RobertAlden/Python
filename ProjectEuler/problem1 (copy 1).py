count = 0
limit = 999

def sumn(n, d):
    n //= d
    return d*n*(n+1) // 2

count = sumn(limit,3) + sumn(limit,5) - sumn(limit,15)
print(count)