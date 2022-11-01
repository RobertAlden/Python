import dependency1
from subdir2 import dependency3,dependency4
from subdir3 import *

print("Hello World")
print(dependency1.multipi(5))
print(dependency1.math.pi)
print(dependency3.neg_mode([1,2,2,4]))
print(dependency4.neg_avg([1,2,2,4]))
print(double_mode([1,2,2,4]))
print(dependency6.double_avg([1,2,2,4]))