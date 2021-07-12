# Assignment 14:
# Write a Python program requesting a name and three numbers from the user. The program will need 
# to calculate the following:
# 
# the sum of the three numbers
# the result of multiplying the three numbers
# divide the first by the second then multiply by the third
# Print a message greeting the user by name and the results of each of the mathematical operations. 
# 
# You must provide a comment block at the top indicating your name, the course, the section, and 
# the date as well as a description of the program. Also, comment as necessary to clearly explain 
# what it is you are doing where you are doing it in the program. 

# This was the first assignment of my second class on learning Python. It wasa mostly a refresher 
# on things that I had already learned from the first class, but there was one significant new 
# thing — storing number inputs as integers from the get go. I also did some additional research 
# to learn how to round the last answer to a set number of decimal places.

Code: 
  
# Request a name and 3 numbers, perform multiple math fucntions on numbers and display results
# Code by AJChestnut
# July 10, 2020

#ask user for name and store as a variable
print ('Hello, there. What\'s your name?')
userName=input()

#Ask user for 3 numbers and store the int value as variables
print('It\'s nice to meet you,', userName + '.')
print('And now, I am going to need 3 numbers from you.')
print('What is your first favorite number?')
firstNum=int(input())
print('Your second favorite number?')
secondNum=int(input())
print('And lastly, what is your third favorite number?')
thirdNum=int(input())

#mathing for winners
sums=firstNum + secondNum + thirdNum
products=firstNum * secondNum * thirdNum
mixed=firstNum / secondNum * thirdNum

#display math results
print('Thank you,', userName + '.', 'The sum of your favorite numbers is:', sums)
print('The product of your favorite numbers is: ', products)
print('The first number, divided by the second number, then multiplied by the third is: ', round(mixed, 2))
