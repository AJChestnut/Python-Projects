# Assignment:
# Implement a random number guessing game. The computer will pick a number 
# at random from 0-9, the user will be asked to guess the number.  
# Inform the user if they get the answer correct.

# This assignment was my first time importing a module into my code. Since this 
# was a class for beginners, that bit of code was given to us in advance. 
# It was fun to puzzle through how best to code this one. I also learned that
# you can add things to your code to make sure the code works, then comment
# them out for the final project. 

#Code:

# Random number from 0-9 guessing game
# Code by AJChestnut
# March 31, 2019

# Create random number and assign to variable
from random import randint
randomNum = randint(0,9)

# Used to simplify testing, no longer needed.
# print(randomNum)

# Assign long string to variable
setUp = """Welcome to my parlor,
I'd like to play a game.
I'm thinking of a number from 0 to 9.
Can you guess what it is?"""
print(str(setUp))

# ask user for guess and assign to variable
guess = input()

# compare guess to rng
if int(guess) == int(randomNum):
    print('You must be psychic! That\'s correct.')
else:
    print('Nope! Hahahahahaa!')
