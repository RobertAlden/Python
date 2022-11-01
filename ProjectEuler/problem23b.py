import math
def divisors(n):
    """
    Returns all nontrivial divisors of an integer, but makes no guarantees on the order.
    """
    # "1" is always a divisor (at least for our purposes)
    yield 1

    largest = int(math.sqrt(n))

    # special-case square numbers to avoid yielding the same divisor twice
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    # all other divisors
    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i

def is_abundant(n):
    if n < 12:
        return False
    return sum(divisors(n)) > n

def is_abundant_sum(n):
   for i in abundants:
       if i > n:  # assume "abundants" is ordered
         return False
       if (n - i) in abundants:
           return True
   return False

abundants = list(x for x in range(1, 28123) if is_abundant(x))
abundants_set = set(abundants)
def is_abundant_sum(n):
   for i in abundants:
       if i > n:  # assume "abundants" is ordered
         return False
       if (n - i) in abundants_set:
           return True
   return False

sum_of_non_abundants = sum(x for x in range(1, 28123 + 1) if not is_abundant_sum(x))
print (sum_of_non_abundants)

print(4190404-4179871)