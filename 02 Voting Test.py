# Assigment 02: 
# Implement a voting test. The user enters their age and then the program prints 
# either, “You must be 18 to vote” or “You are of voting age”.

# This was part of a 4 program series designed to teach about conditional logic.
# For this I had to take a user's age and compare it to the number 18.
# It contains one of my first if else statements.


# Week 3 Voting Test to determine if user is of age to vote
# Code by AJChestnut  
# March 27, 2019

#Ask user for their age, then store input in variable
print('How old are you, citizen?')
myAge=input() #string

#if statement to compare input to voting age requirement
if int(myAge) >= 18:
    print('You are of voting age.')
else:
    print('You must be 18 to vote.')
