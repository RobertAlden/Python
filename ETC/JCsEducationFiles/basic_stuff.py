"""
#include <iostream>

using namespace std;

int main(){
    cout<<"Hello World"<<endl;
    return 0;
}

from random import randint

number_to_guess = randint(0, 1000)
while True:
    print("Guess a number between 0 and 1000: ")
    guess = int(input())

    if guess > number_to_guess:
        print("Lower!")
    elif guess < number_to_guess:
        print("Higher!")
    else:
        print("You got it!")
        break
"""

limit = 1000000
print(f"Now its your turn! Input an integer between 0 and {limit} and the computer will guess it.")
number_to_guess = int(input())
current_ceiling = limit
current_floor = 0


while True:
    guess = (current_ceiling - current_floor) // 2
    if guess > number_to_guess:
        current_ceiling = guess
    elif guess < number_to_guess:
        current_floor = guess
    else:
        print("The computer got it!")
        print("It took the computer " + str(len(guesses)) + "guesses, and those guesses were: \n", guesses)
        break



