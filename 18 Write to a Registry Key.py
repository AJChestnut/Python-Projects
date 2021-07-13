# Assignment 18:

# Write a program that takes a value from a user and stores it in the registry. You can use 
# any key name that you like but also store the current time as another value inside of your 
# new key. Finally, get a directory listing of your current working directory and store that 
# value. You may need to use REG_MULTI_SZ for that value. 

# This assignment was the most complicated I had ever had to write. Working with the registry
# was complex and required a lot of work to hand the appropriate information to the addKey function.
# In my first attempt at this assignment, I also forgot to add error handling to the addKey function.
# I have corrected that since and this is my final code.

# Code:

#####
# Create a registry entry
# Code by AJChestnut
# 08-09-2020
#####

import os
import winreg
import time

######
# function: addKey
# purpose: Accept user input and assign to registry key
# inputs: key value
# returns: nothing
######
def addKey(x, y):

    keyName = "myKeyDamnit" #store key name as variable

    #establish where to create new key
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\" + keyName)

    #set value inside newly created key
    try:
        winreg.SetValue(key, y, winreg.REG_SZ, x)
    except OSError:
        print("Error setting key value: " + OSError)

######
# function: getCWD
# purpose: gets the current working directory and contents
# inputs: none
# returns: the files in the current working directory
######
def getCWD():
    myCWD = os.getcwd() #finds the current working directory and saves it to variable
    return str(os.listdir(myCWD)) #returns files in the current working directory

######
# function: getTime
# purpose: gets current system time
# inputs: nothing
# returns: current system time
######
def getTime():
    now = time.time() #gets epoch time
    return time.ctime(now) #converts epoch time to strings


print("What would you like the value to be?")
userValue = input() #store user supplied input into variable

addKey(userValue, "AValue") #send key and value to function

addKey(getCWD(), "Current Working Directory") #send key and value to function

addKey(getTime(),"time stamp") #send key and value to function
