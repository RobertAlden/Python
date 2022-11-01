sums = []
for i in range(100):
    for k in range(100):
        sums.append(sum([int(i) for i in list(str(i**k))]))
print(max(sums))