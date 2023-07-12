''' A basic guessing game where a random number is generated and the user tries to guess it

Author: SW


Date: 12/07/2023
First version, just a practice.

No error handling
'''

import math

def interaction():

    """ Ask the user if they want to play a guessing game"""
    
    x = input("Would you like to play a guessing game (y/n)? ")

    while True:
        #In the main code block, the bool value here will be used.
        #maybe change later, doesn't seem right atm.
        if x == "y" or "Y":
            return True
        else:
            return False


def game():
    ''' A function to ask the user for input, and compare it to a random number
'''
    user_guess = input("Please enter your guess, a number between 1 and 10")

    #Check if the user inputed an integer between 1 and 10
    if isinstance(user_guess, int) and user_guess > 0 and user_guess <= 10:
        if user_guess == math.randint(1,10):
            print("You guess correctly!")
    else:
        print(f"You guessed incorrectly. The answer was {user_guess}")

def main(): 
    if interaction():
        game()
    else:
        exit()
    interaction()

if __name__ == '__main__':
    main()

