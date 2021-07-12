# Assignment:
# Write a program that counts down from 10. Implement your program first with a while loop.  
# Now implement your program with a for loop. Include both versions in your submission file.

# While loops and for loops. Learning how to take the contents of a variable, modify it, and then reassign
# it to the same variable was eye opening. 

# Code:

# Code by AJChestnut
# April 7, 2019

#Counting down from 10 with a while loop

count = 10 #Int

while count >= 0:
    print(count)
    count -= 1

#Coutning down from 10 with a for loop

for count in range(10, -1, -1):
    print(count)
