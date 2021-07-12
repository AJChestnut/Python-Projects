# Assignment:
# Ask the user to enter a grade percentage.  Convert the grade into a letter grade.  
# For instance, if the user types 99 then print A+.

# This was my first time working with elif statements. It was interesting to see
# how you sent up so many different options and then using logic have the script
# determine which is the correct answer. Also, lots of use out of the escape character.

# Code:

# Grading scale, percentage to letter grade converter
# Code by AJChestnut
# March 31, 2019

# ask user for their grade and store in variable
print("I got a 95! What did you get on the test?")
myGrade=input() #string

# compare user input with grading scale and print corresponding letter grade
if int(myGrade) >= 97:
    print('Great job! That\'s an A+!')
elif int(myGrade) >= 93:
    print('Great job! That\'s an A!')
elif int(myGrade) >= 90:
    print('Great job! That\'s an A-!')
elif int(myGrade) >= 87:
    print('Good job! That\'s a B+!')
elif int(myGrade) >= 83:
    print('Good job! That\'s a B!')
elif int(myGrade) >= 80:
    print('Good job! That\'s a B-!')
elif int(myGrade) >= 77:
    print('You passed! That\'s a C+.')
elif int(myGrade) >= 73:
    print('You passed! That\'s a C.')
elif int(myGrade) >= 70:
    print('You passed! That\'s a C-.')
elif int(myGrade) >= 67:
    print('Yeesh, that\'s a D+.')
elif int(myGrade) >= 63:
    print('Yeesh, that\'s a D.')
elif int(myGrade) >= 60:
    print('Yeesh, that\'s a D-.')
elif int(myGrade) < 60:
    print('Ouch, that\'s an F!')
