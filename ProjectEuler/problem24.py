import itertools
key = 1000000
size = 9

permutations = list(map("".join, itertools.permutations('0123456789')))


print(permutations[key-1])