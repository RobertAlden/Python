
def miller_rabin(n,a):
    d = (n-1)
    while (d % 2 == 0):
        d //= 2
    result = all([pow(tests,d,n) in [1,n-1] for tests in a])
    return result

t = [2,3,5]
answer = sum(t + [i for i in range(1,1999999,2) if miller_rabin(i,t)])
print(142913828922 - answer)
