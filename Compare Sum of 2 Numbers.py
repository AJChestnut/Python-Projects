# Assignment:
# Write a program that asks for two numbers. If the sum of the numbers is greater 
# than 100, print "They add up to a big number" if it is less than/equal to 100 
# than print "They add up to ____".

# This assignment was also part of a 4 part assignment using comparative logic.
# I learned about defining variable and ensuring that they are the type you need
# them to be for the actions you wish to take on them. For instance, if I tried
# to add the two user input variables together without converting them to integers 
# first, my program would not have worked. 

#Code:

# Compare the sum of 2 numbers to 100
# Code by AJChestnut
# March 31, 2019

# ask user for 2 numbers and assign to variables
print('I\'m going to ask you for two numbers.')
print('What would you like the first number to be?')
number1 = input() #string
print('Good. And what would you like the second number to be?')
number2 = input() #string

#add the two numbers together and assign to variable
total = int(number1) + int(number2) #int

if total > 100:
    print('They add up to a big number.')
else:
    print('They add up to ' + str(total) + '.')
