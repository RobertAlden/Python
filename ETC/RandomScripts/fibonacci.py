from functools import cache
import sys
sys.setrecursionlimit(15000)

@cache
def fibonacci(n):
    #print("HELLO")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(1200))