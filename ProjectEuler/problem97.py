#print(28433 * (2**7830457) + 1)


iterations = 7830457
x = 2
for i in range(2,iterations+1):
    x *= 2
    if len(str(x)) > 10:
        x = int(str(x)[-10:])
    #print(x,i)

x *= 28433
x += 1
x = int(str(x)[-10:])
print(x)