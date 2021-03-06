# Assignment #1:
# Write a program that has a conversation with the user. 
# The program must ask for both strings and numbers as input.
# The program must ask for at least 4 different inputs from the user.
# The program must reuse at least 3 inputs in what it displays on the screen. 
# The program must perform some form of arithmetic operation on the numbers the user inputs.
# Please include comments in your code to explain how it works

# This is the first piece of coding I really ever wrote. 
# This assignment taught me about storing strings and numbers in variables.
# As well as, manipulating them with concatination. 


# Code:
# This is my Conversation with a Computer Assignment Program
# print('\n') used for aesthetic purposes
# Code by AJChestnut
# March 24, 2019

# Define intro as a variable
hello = """Hello! Welcome to my Magical MultiPlex.
Where we have access to every movie in the multiverse.
Even the ones you just made up!
Now, what is the title of the movie you would like to see?"""
print(hello)

#Ask user for movie selection and define response as variable
movie=input() #string
print('\n')
print('Ah, ' + str(movie) + ', one of my favorites.')

#ask user for preferred show time and define as a variable
showStart = """Used to watch it all the time when I was a lad.
And what time would you like the show to start?"""
print(showStart)

showTime = input() #string
print('\n')

#confirm showtime and ask how many tickets they'd like to buy
print('Can do, show to start at ' + str(showTime))
print('And how many tickets would you like?')

tickets= input() #string
print('\n')

#Converts string to int and finds total sale price for requested tickets
total = int(tickets)*11 #int

print('Right, ' + str(tickets) + ' and at a price of 11 dollars a ticket your total is ' + str(total) + ' dollars.')
print('Would you like an escort to your seat?')

#final response is unchanged regardless of user input
input() #input not stored
print('\n')

print('Of course. I do hope you enjoy your show.')
print('And if you have any problems, please feel free to let me know.')
