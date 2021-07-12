# Assignment 12:
# Say you have a list of lists where each value in the inner lists is a one-character string, like this:
# 
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. 
# The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.
# 
# Copy the previous grid value, and write code that uses it to print the image.
# 
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

# This extra credit assignment also took me longer than the main two assignemnt for the week. Something about nested for loops takes
# my brain a while to process and understand the order of how things are going to go. Also, finding the right indentation for the 
# print new line command took a few tries.

# Code:

# Character Picture Grid
# Code by AJChestnut
# April 14, 2019

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for a in range(0,6): #establish grid coordinates for the horizontal
    for b in range(0,9): #establish grid coordinates for the verticle
        print(grid[b][a], end='') #grab character from each verticle row and print without new line
    print('\n') #once a row is complete, make a new line
