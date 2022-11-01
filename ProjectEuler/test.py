# http://radiusofcircle.blogspot.com

# time module
import time

# time at the start of program execution
start = time.time()


def is_lychrel(n):
    """this function will check if the number
    is lychrel number or not"""
    # fifty iterations
    for i in range(50):
        # sum of number and reverse
        number = n + int(str(n)[::-1])
        # if is palindrome
        if str(number) == str(number)[::-1]:
            return False
        n = number
    return True

# counter to count
counter = 0

# looping till ten thousand
for i in range(10001):
    if is_lychrel(i):
        counter += 1

# printing the counter
print(counter)

# time at the end of program execution
end = time.time()

# total time of execution
print(end - start)