attempts = list(set([319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]))
attempts.sort()
attempts = [list(str(i)) for i in attempts]
print(attempts)


# digits = [0]*10

# for i in attempts:
#     for k,c in enumerate(list(str(i))):
#         digits[int(c)] += ((k+1)*10)**2

# digits = [[i,k] for i,k in enumerate(digits)]

# digits.sort(key=lambda a : a[1])

# print(digits)

# digits = [str(i) for i,k in digits if k != 0]

# print("".join(digits))

