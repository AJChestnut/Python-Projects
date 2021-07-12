# Assignment 10:
# Say you have a list value like this:
# listToPrint = ['apples', 'bananas', 'tofu', 'cats']
# Write a program that prints a list with all the items separated by a comma and a space, 
# with and inserted before the last item. For example, the above list would print 'apples, 
# bananas, tofu, and cats'. But your program should be able to work with any list not just 
# the one shown above. Because of this, you will need to use a loop in case the list to 
# print is shorter or longer than the above list. Make sure your program works for all 
# user inputs. For instance, we wouldn't want to print "and" or commas if the list only 
# contains one item.

# The initial while loop that allows a user to input variables to a list was given to us
# by the instructor. We were responsible for creating the rest of the script. The first two
# if statements were the easy part of this assignment for me. If this, do that. Working to
# create the for loop that went through every variable and had a step to change the output
# for the last variable in the list was complicated for me. It took a few different iterations
# before I wrote this one that worked. I've got to admit, I also spent longer than I probably 
# should have on deciding to end the list with a period or not.

# Code:

# Comma Code
# Code by AJChestnut
# April 14, 2019

listToPrint = []    #create variable with empty list
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "": #If nothing input, stop adding things to list
        break
    else:
        listToPrint.append(newWord) #If something input, add to end of list

if len(listToPrint) == 1: #if only 1 value in list, print value
    print(str(listToPrint[0]))

if len(listToPrint) == 2: #If only 2 values, comma not needed just the "and"
    print(str(listToPrint[0] + ' and ' + str(listToPrint[1])))

if len(listToPrint) > 2:
    for newWord in listToPrint[:-1]: #print item + comma and space until the last value in list
        print(str(newWord) + ', ', end='')
    print('and ' + str(listToPrint[-1])) #finish list with "and" preceeding final value
