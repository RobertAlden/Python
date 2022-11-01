limit = 10000000

numbers = [[i,1] for i in range(1,limit)]


def square_digit_sum(n):
    return sum([int(c)**2 for c in str(n)])


def process_list(l):
    for i in l:
        v = i[0]
        c = i[1]

        new_v = square_digit_sum(v)
        l[new_v-1][1] += c
        i[1] = 0
    l = [i for i in l if i[1] != 0]
    return l

#print(numbers)
#print(process_list(numbers))

def process_list_two(l):
    for i in l:
        v = i[0]
        c = i[1]

        new_v = square_digit_sum(v)
        for k in l:
            if k[0] == new_v:
                k[1] += c
                break
        else:
            l += [[new_v,c]]
        i[1] -= c
    l = [i for i in l if i[1] != 0]
    return l

while len(numbers) > 10:
    numbers = process_list_two(numbers)
    print(len(numbers))
    
sums = 0
for k in numbers:
    sums += k[1]

sums -= numbers[0][1]

print(sums)