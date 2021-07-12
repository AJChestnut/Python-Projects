# Assignmnet 16:

# Take the master boot record from this week's module and use it as a file input for your
# program. It will be named block.dd and you can assume that it's in your current directory 
# so you don't have to provide a path to it. Make sure that you copy it into the directory 
# where your Python file is located or your program will fail. 

# Use the information in the Wikipedia entry for Master Boot Record to write a program 
# that will parse a portion of the partition table. The first partition entry is located 
# at the address 1BE (hex). Print out the status byte (1 byte located at the starting address), 
# the partition type (1 byte located at the address 1BE + 4) and the address of the first 
# sector in the partition (1BE + 8). 

# This assignment was the first time I opened a file and accessed the information it contained. \
# It gave me a significant amount of trouble. I didn't know it was a binary file. Nor did I know
# that you had to use a different option to open binary files. I spent a long time trying to
# figure out why my `open("block.dd", "r")` wasn't working. 

# Code:

#####
# Data Manipulation
# Code by AJChestnut
# 7/26/2020
#####

import struct

#####
#function: open_file
#purpose: Opens the file and reads into a bytearray
#inputs: Binary file
#returns: bytearray
#####
def open_file():
    with open("block.dd", "rb") as f:
        chunk = f.read()
    return chunk

######
# function: getUnpackValue
# purpose: Unpack more than 1 byte of binary data
# inputs: Address range
# returns: List of integer values for the byte range
######
def getUnpackValue(x):
    #Unpack the binary range
    myList = struct.unpack("<i", x)

    #Return the integer list for range
    return myList

#make chunk a bytearray
chunk = bytearray()
#add the bytes from the open_file function to chunk
chunk += open_file()
#give byte range to getUnpackValue function and receive integer as a list
result = getUnpackValue(chunk[0x1BE+8:0x1BE+12])

#print the different bytes as integers
print('Status Byte:', chunk[0x1BE])
print('Partition Type:', chunk[0x1BE+4])
print('First Sector Address:', result[0])
