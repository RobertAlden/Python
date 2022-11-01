"""
Topics: Iteration, Lists, List comprehensions, Indexes and Slicing, Sorting
Bonus Topic: Functions
"""
from random import randint

# For loops with range
for i in range(10):
    print(i, end=" ")
print("")

# For loops with range using start stop
for i in range(1,10):
    print(i, end=" ")
print("")

# For loops with range, using start, stop, and interval
for i in range(1,10,2):
    print(i, end=" ")
print("")


# For loops to create a list
length = 11
my_list = []
for _i in range(length):
    my_list.append(randint(1,10))
print(my_list)


# For loops to iterate over a list the "normal way"
for i in range(len(my_list)):
    print(mylist[i], end=" ")
print("")

# For loops to iterate over a list the python way
for i in my_list:
    print(i, end=" ")
print("")

# For loops to iterate over a list while tracking current index
for k,i in enumerate(my_list):
    print(str(k) + ":"+str(i), end=" ")
print("")

# Slice Notation
print("Plain List: \n",my_list)
print("Second index of the list: \n",my_list[2])
print("The List from the second index onwards: \n",my_list[2:])
print("The List from the second index to before the sixth index: \n",my_list[2:6])
print("The List from the second index up to the tenth, only every third index: \n",my_list[2:10:3])
print("The last index of the list (regardless of size): \n", my_list[-1])
print("The List but in reverse: \n", my_list[::-1])


# Why list comprehensions exist:
print(my_list)
new_list = []
for i in my_list:
    new_list.append(i*10)
print(new_list)

new_list = [i*10 for i in my_list]
print(new_list)

# List comprehensions can have conditionals:
new_list = [i*10 if i % 2 == 0 else i for i in my_list ]

