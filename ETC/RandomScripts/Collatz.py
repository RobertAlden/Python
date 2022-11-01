def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return int(n//2)
    else:
        return int(3 * n + 1)

iters = []
maximum = []
for i in range(27,32):
    k = i
    c = 0
    max_ = 0
    while k != 1:
        print(k)
        k = collatz(k)
        c += 1
        if k > max_:
            max_ = k
    maximum += [max_]
    iters += [c]

print(iters)
print(maximum)
