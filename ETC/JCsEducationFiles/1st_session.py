from random import randint
'''
if 1 == 1.0:
    print("Yep seems good")
else:
    print("WHAT")

#print("we done here")

lower_bound = 10
upper_bound = 40

number = randint(lower_bound,upper_bound)
print(f"input a number between {lower_bound} and {upper_bound}")
while True:
    guess = int(input())

    if guess > number:
        print("Lower!")
    elif guess < number:
        print("Higher!")
    else:
        print("You got it!")
        break
'''
import time



lower_bound = 1
upper_bound = 10000000000000000000000000000000000000000

print(f"input a number between {lower_bound} and {upper_bound}" )
number = int(input())
guesses = []

while True:
    guess = (upper_bound + lower_bound) // 2
    guesses.append(guess)
    if guess > number:
        upper_bound = guess
    elif guess < number:
        lower_bound = guess
    else:
        print("The computer got it!")
        print("The computer made " + str(len(guesses)) + " guesses.")
        print(guesses)
        break
    time.sleep(0.01)

