# Assignment:
# Extend your guessing game from last week.  Write a program that picks a random number from 1-100.  
# Then ask the user to guess a number. Tell the user if the answer is higher or lower than the number 
# they guessed, or if they got the correct answer.  Allow them to guess again if they got the guess incorrect.  
#They should be able to guess numbers an infinite number of times until they get the correct answer, at which point your loop will end.

# This script took me a while to figure out. The idea of adding if statements to the while loop was new to me.
# I do like how it turned out in the end. Also, assigning the input to a variable after the two if statements
# was a breakthrough for me. I also continued the practice of adding code for testing purposes and then commenting
# it out once I was done.

# Code: 

# Guessing game from 1 to 100
# Code by AJChestnut
# April 7, 2019

from random import randint
randomNum = randint(1,100) #generate random number

print('Hello, I\'m thinking of a number from 1-100.')
print('Can you guess what it is?') # ask user to guess number

# print(randomNum) I included this so I could see if it was working correctly during testing, commented out, once complete.

answer=input() #string

while int(answer) != randomNum: #if they guess wrong
    if int(answer) > randomNum: #compare guess to random and provide feedback
        print('Smaller!')
    if int(answer) < randomNum: #compare guess to random and provide feedback
        print('Bigger!')
    answer=input() #let them guess again
if int(answer) == randomNum: #if they guess correctly, congratulate and end program
    print('You got it!')
