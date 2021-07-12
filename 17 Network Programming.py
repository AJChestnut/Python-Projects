# Assignemnt 17:

# This week, you are going to build on the program from last week. Use the same file from last week. 
# You will be extracting the first partition entry from the master boot record that is contained in 
# the file. The first partition entry starts at offset 0x1BE and ends at 0x1CD. Pull that chunk of 
# bytes out of the file provided and send it to the server software that you will write. The server 
# will listen for the chunk of data and print out the status of the drive, the partition type and 
# the starting address of the partition as an integer. 

# You can refer to Wikipedia (Links to an external site.) for additional details about offsets within 
# the master boot record and partition table for the pieces of information you are looking for. 

# This assignment is a two parter. The first section of code is the extention from the previous
# assignemnt. I took what I had already written and added a function that creates a socket for this script to send the 
# data to the server script. The server script will follow the client script.

# Setting up the client side socket was fairly easy. They seem pretty standard. I also had all of the other
# code written, so this was fairly quick. Determining which data to send to the server howerver, took some 
# trial and error. Then, when it came to writing the server code, I was able to copy over a lot of the client
# code and then add the listening socket for the server. 

# Client Code:

#####
# Data Manipulation - Network Programing Client
# Code by AJChestnut
# 7/26/2020 - 8/2/2020
#####


import struct

import socket

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

######
# function: servClient
# purpose: Creates the client socket to send data to server
# inputs: Binary data
# returns: N/A
######
def servClient():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('127.0.0.1', 1550))

    s.send(chunk)
    resp = s.recv(2048)
    s.close()

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

#run client
servClient()


# Server Code:

#####
# Network Programming
# Code by AJChestnut
#7/26/2020
# server receives and prints data


import socket

import struct

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

######
# function: servServer
# purpose: Creates server socket to receive and print data
# inputs: Binary data from client
# returns: N/A
######
def servServer():
    #creates socket and binds to loopback ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 1550))

    #Max clients to connect with at once
    s.listen(5)

    len = 2048

    #Main loop of server
    while 1:
        (c, address) = s.accept()
        data = c.recv(len)
        #If any data was received, run unpack of binary and print results
        if data:
            result = getUnpackValue(data[0x1BE+8:0x1BE+12])

            #print the different bytes as integers
            print('Status Byte:', data[0x1BE])
            print('Partition Type:', data[0x1BE+4])
            print('First Sector Address:', result[0])
            c.close()

#runs server to receive and print data
servServer()
