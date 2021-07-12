# Assignment 13:
# We will be extending the Caesar cypher we looked at earlier into a full-fledged password saver. The program will be able to:
# 
# Lookup passwords for websites
# Add new passwords for websites (encrypting them with the caesar cypher)
# Store these passwords to a file on the computer
# Load passwords from a stored password file
# Most of the code is provided but there are some critical components missing. You will need to add these components.
# 
# A first draft is due at the end of Week 6. This is your opportunity to get feedback and support on this assignment. 
# The final version is due at the end of Week 7. Week 7 ends on a Friday, so don't wait until the last minute!
# 
# Create a python file called PasswordSaver.py in PyCharm and copy the following code into it.
# 
# Extra Credit (max 5 points): Add additional menu items to the program. For instance, add the ability to delete passwords.


# This assignment was the final project for this class. We were given two weeks to finish writing this script. 

# The assignment asked for two things. The first being, write the code for Choice 2, look up a password. The assignment
# gave us some guidance on what to do for this part. Even with the guidance, finding the right levels of indentation to 
# ensure everythinig happened in the order I needed it too took some time. 

# The second ask, was to write the code for choice 3, add a new website and password. 
# The encryption mechanism was already created for us, which took a big chunk of the work off of our shoulders.
# So, that left taking the website and password that the user input, encrypt the password using the already 
# established caesar cypher, add that information to a new list, and then append the new list to our master list. 
# This part was relatively easy. All we needed was 1 line to create the new list, and another to append it.

# There was also an extra task we could do. We could add a new option to the script. I chose to create an
# option to delete one of the passwords from the list. As is the trend, the extra credit parts continue to be
# the most difficult. I am proud of how it turned out, though. 

# I made it so the script would print out all of the website names that are stored in the list, 
# to made it easier for the users to enter the correct website name. 

# I then added a confirmation, so that the users would have to ask to delete the password twice, helping 
# to ensure that they wouldn't accidentally delete the wrong password. If they confirmed, I'd have the 
# script iterate through the master list and if the website that the user entered matched a website in the list
# it would delete the matching list. 

# Working with lists inside of lists took me a little while to get used to but by the end of this 
# assignment, I felt like I had a good grasp on it. 

# Code:

# Password Saver
# Code added by AJChestnut
# April 21, 2019

import csv
import sys

#The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]


#The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

#The encryption key for the caesar cypher
encryptionKey=16

#Caesar Cypher Encryption
def passwordEncrypt (unencryptedMessage, key):

    #We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    #For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)



while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Delete a Password")
    print(" 6. Print the encrypted password list (for testing)")
    print(" 7. Quit program")
    print("Please enter a number (1-7)")
    choice = input()

    if(choice == '1'): #Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'): #Lookup a password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        ####### Begin YOUR CODE HERE ######

        for i in range(len(passwords)): #iterate through the lists
            if passwords[i][0] == passwordToLookup: #if the user input equals the value in the first position of each list
                print('The password is: ' + passwordEncrypt(str(passwords[i][1]), -16))  #print the decrypted value stored in the password position

        ####### End YOUR CODE HERE ######

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        ####### Begin YOUR CODE HERE ######

        encryptedPassword = passwordEncrypt(unencryptedPassword, 16) #encrypt the new password
        newList = [website, encryptedPassword] #create list with website name and encrypted passsword
        passwords.append(newList) #add new list to passwords list

        ####### End YOUR CODE HERE ######

    if(choice == '4'): #Save the passwords to a file
            savePasswordFile(passwords,passwordFileName)
            print('File Saved.') #confirmation messages make me feel better

        ####### Begin YOUR CODE HERE ######

    if(choice == '5'):
        print('Which website\'s password would you like to delete?')
        for keyvalue in passwords:
            print(keyvalue[0])
        delWebsite = input()

        print('Are you sure you want to delete the password for ' + str(delWebsite) + '?')
        print(' 1. Yes')
        print(' 2. No')
        print('Please enter 1 or 2.')
        confirm = input()

        if(confirm == '1'):
            for i in range(len(passwords)): #iterate through the lists
                if passwords[i][0] == delWebsite: #if the user input equals the value in the first position of each list
                    del passwords[i]  #delete the list from passwords
                    print(str(delWebsite) + '\'s password has been deleted.') #confirmation message, Yay!
                    break

        if(confirm == '2'):
            continue

            ####### End YOUR CODE HERE ######

    if(choice == '6'): #print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '7'):  #quit our program
        sys.exit()

    print()
