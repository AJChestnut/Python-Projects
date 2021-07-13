# Assignment 19:

# In this week's module, you will find a History database  downloadthat was taken from Google Chrome. 
# You will be using this History file to get the list of Web addresses that the user has visited. 

# You will write a program that will take this database file and extract the Web addresses that 
# the user visited, the number of times the page was visited and the last time it was visited.
# The last time will not be readable by humans but you don't have to worry about converting it for
# the purposes of this program. The schema from the database is below. Find the correct table that
# you need to query and the correct columns from that table. 

# When I initially wrote this code, I was marked down for not having enough functions. I thought that
# functions were used for segments of code that you would have to run multiple times, there aren't 
# any of those in this code. I have reworked it to include functions. I also didn't have enough 
# exception handling. So, I spent more time thinking about where there were instances that could 
# generate exception and added in some failsafes.

# Code:

#Jake Eaton
#CYBR-260-45 Security Scripting with Python
#08-16-2020
#Week 6: Programming assignment
#Using Python to pull and display information from a database

import os
import sqlite3

######
# function: getDbPath
# purpose: Get the database's file path
# inputs: Database name
# returns: database's file path
######
def getDBPath(dbName):

    #Directory variable
    DIR_NAME = os.path.dirname(__file__)
    try:
        db_path = os.path.join(DIR_NAME, dbName)
    except OSError as e:
        print("Cannot create path: " + e)

    return db_path

######
# function: closeDB
# purpose: Close the connection to the database
# inputs: SQL connection
# returns: Nothing
######
def closeDB(sqlConn):

    try:
        sqlConn.close()
    except sqlConn.error as e:
        print("Unable to close the database: " + e)
        exit(1)

#saves the database's file path to a variable
db_path = getDBPath("History.db")

#try block incase there is an error connecting to the database file
try:
    sqlConn = sqlite3.connect(db_path)
except sqlConn.DatabaseError as e:
    print("unable to open database " + e)
    exit(0)

#since this is after the try block, it lets you know the database was accessed successfully
print("Database opened successfully", "\n")

#Gives a header to the output
print("The urls / # of visits / time of last visit in the history are:", "\n")

#selects everything from the urls table
dbLoc = sqlConn.execute("SELECT * FROM urls")

#for every row in the table this prints the requested information along with a header describing what it is
for row in dbLoc:
    print("url:", row[1], "\n", "# of Visits:", row[3], "Time Visited:", row[5], "\n")

#closes the connection to the database
closeDB(sqlConn)
