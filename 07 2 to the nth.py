# Assignment 07:

# Write a program that prints 2n where n goes from 1 to 100. Print one answer per line 
# (note: you are answering the question, how high can you count on 100 fingers). 
# Write your program using a 'for' loop.  Reminder '**' is the operator for exponents, 
# so for example 4**3 is 4 to the third power, or 4 * 4 * 4 which equals 64. 

# I have no idea why I chose finger, your guess is as good as mine.

# 2 to the nth from 1 to 100
# Code by AJChestnut
# April 7, 2019

nth = 1 #int

for finger in range(0, 100):
    count = 2 ** nth
    print(count)
    nth += 1
