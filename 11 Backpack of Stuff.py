# Assignment 11:

# Complete the following code. Fill in the two sections of code identified in the comments.
# 
# import sys
# 
# itemsInBackpack = ["book", "computer", "keys", "travel mug"]
# 
# while True:
#     print("Would you like to:")
#     print("1. Add an item to the backpack?")
#     print("2. Check if an item is in the backpack?")
#     print("3. Quit")
#     userChoice = input()
# 
#     if(userChoice == "1"):
#         print("What item do you want to add to the backpack?")
#         itemToAdd = input()
# 
#         ####### YOUR CODE HERE ######
#         #add the item to the backpack
#         ####### YOUR CODE HERE ######
# 
#     if(userChoice == "2"):
#         print("What item do you want to check to see if it is in the backpack?")
#         itemToCheck = input()
# 
#         ####### YOUR CODE HERE ######
#         #Print out if the user's item is in the backpack
#         ####### YOUR CODE HERE ######
# 
#      if(userChoice == "3"):
#         sys.exit()

# This assignment was given to us with a large part of this script already written. We were responsible for 
# two parts. The first, was writing the code to add the item that the user entered into the list. Which seemed
# almost too easy. All we needed was one line of code. The second, was checking to see if a user entered value 
# was contained in the list. This was the meat of the assignment. The most challenging part for me was remembering
# to ensure that I wasa trying to print the string value of the item in the list.

# Code:
# Backpack Full of Stuff
# Code by AJChestnut
# April 14, 2019

import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if(userChoice == "1"):
        print("What item do you want to add to the backpack?")
        itemToAdd = input()
        ####### YOUR CODE HERE ######
        itemsInBackpack.append(itemToAdd) #add the item to the backpack
        ####### YOUR CODE HERE ######


    if(userChoice == "2"):
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()
        ####### YOUR CODE HERE ######
        if itemToCheck in itemsInBackpack: #check if value is in the list, if it is, say so
            print('Yes! ' + str(itemToCheck) + ' is in the backpack.')
            print('\n')
        if itemToCheck not in itemsInBackpack: #check if value is not in the list, if it isn't, say so
            print('I\'m sorry, no. ' + str(itemToCheck) + ' is not in the backpack.')
            print('\n')
        ####### YOUR CODE HERE ######


    if(userChoice == "3"):
        sys.exit()
