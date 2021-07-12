# Assignment 15:

#This week, you will write another program. This time, you will do the same thing twice. 
# 
# First, take a set of 6 grades from a user and average them. Provide the average to the user. You need to check to make 
# sure the grades are within the normal range. If the grade is less than 0 or more than 100, issue a warning to the user. 
# You don't need to take the grade again, just let the user know. 
# 
# Second, ask the user how many grades they have. Ask for all the grades and again provide an average. Make sure to check 
# that the grades are within the normal range as above and issue a warning to the user. 
# 
# For any function you use, use the following comment block as before the function to document it. 
# 
# # function: name
# 
# # purpose: 
# 
# # inputs: 
# 
# # returns:  
# 
# Fill in the sections as necessary for what you are doing. Document your code as in your previous 
# programming assignment, including the attribution block indicating your name, class, etc. Include 
# text or screen captures indicating your program works. 

# This assignment had me working with functions. Functions were a strange concept to me. I understand 
# the usfulness of defining code that repeats in the scripts as a function, however, it was difficult 
# for me to understand how to place them in the code to make proper use of them. I thought about coding 
# it so that if the user entered in a number outside of the acceptable range, it would produce and error 
# message and let them try again, but in reading the assignment, I decided that that was out of scope 
# for this project. 

# Code:

# Averaging Grades
# Code by AJChestnut
# 07/19/2020


#function: grade_check
#purpose: To ensure the grade is in the acceptable range
#inputs: the int value of the user's grades
#returns: Warning if outside of range
def grade_check(x):
  if (x > 100):
    print("That grade is more than 100")
  elif (x < 0):
    print("That grade is less than zero")

#function: average
#purpose: find the mean of the list
#inputs: list of grades
#returns: mean of the list
def average(gradeList):
    return sum(gradeList) / len(gradeList)

#create an empty list
gradeList=[]
#create a var to make the prompts look better
gradeNum=1

#prompt user to enter 6 grades
print('Please enter your 6, 0-100 scored, grades that you would like averaged.')
#get 6 inputs from the user
for r in range (6):
    print("Grade #",gradeNum, '?', sep='')
    userGrade = int(input()) #create int var for user input
    gradeNum+=1 #counting variable to make the prompt cleaner
    gradeList.append(userGrade) #add grade to list
    grade_check(userGrade) #call grade_check funciton to determine range

#print list to show grades
print('Your 6 grades were:', gradeList)

#call average function and assign return to var
gradeAvg=average(gradeList)

#print mean of 6 grades
print('The average of your grades is', round(gradeAvg, 2))

#returns the list to an empty state
gradeList=[]
#resets the counting variable
gradeNum=1

#Ask user for number of grades to average
print('How many 0-100 scored grades would you like to average?')
gradeCount=int(input()) #assign # of grades to var
for r in range (gradeCount): #interate through # of grades
    print("Grade #",+gradeNum, sep='')
    userGrade = int(input()) #create int var for user input
    gradeNum+=1 #counting variable to make the prompt cleaner
    gradeList.append(userGrade) #add grade to list
    grade_check(userGrade) #call grade_check funciton to determine range

#print list to show grades
print('Your', gradeCount, 'grades were:', gradeList)

#call average function and assign return to var
gradeAvg=average(gradeList)

#print mean of the grades
print('The average of your', gradeCount, 'grades is: ', round(gradeAvg, 2))
