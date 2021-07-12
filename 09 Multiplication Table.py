# Assignment 09:
# Extra Credit - 5 possible points - Write a program that generates the multiplication 
# table for numbers 1-10. Use two for loops to complete your program. You will need to 
# put one for loop inside of the other for loop. As an extra challenge, see if you can 
# get the indention to look correct.

# For an extra 5 points out of a possible 100, this took me longer than the other 3 
# scripts in this assignment combined. While I ended up simplifying it down to a 
# consise 4 lines of code, this project started out as a mess. It took me a long time
# to wrap my head around the order of operations for a for loop inside of a for loop.
# After that, trying to get the output to format into a nice grid took a lot of researching.

# Code:

# generating the multiplication table for 1-10
# Code by AJChestnut
# April 7,2019

for b in range(1,10): #create first range for vertical
    for c in range(1,10): #create second range for horizontal
        print(b * c, end="\t")  #multiply together to make the table with the \t to help with formatting
    print('\n') #print a new line after each iteration so it's not all on one line
