# Assignment 20:
# Write a program that gets the root document ("/") from *****.edu and extracts every 
# line that has an anchor tag, indicating that it's a hyperlink to another page. The anchor tag
# will start with <a so you can search for that. Ideally, include a space after the a so you only 
# get the anchor tags. 

# Create a Sqlite database sending in the following query at the beginning of your program if 
# the database doesn't exist (use the os module to check to see if a file exists). 

# CREATE TABLE storage(curtime TEXT, line TEXT)

# You can use the following query to insert values into the database:

# INSERT INTO storage (curtime, line) values ('', line);

# With appropriate values for your values. You will need to create a string by concatenating your
# values before you pass the INSERT statement into the execute method. There are a number of ways
# to do this, so be sure to look up examples online. You should be getting the current time each 
# time you enter a value into the database and pass that in for the value of curtime. The following
# will get you the current time with high precision. 

# import datetime

# current_time = datetime.datetime.now().time()

# Use all the same documentation requirements you have been using and submit your program here. 

# NOTE: This assignment used to have you connect to www.*****.edu but that site now redirects to
# HTTPS and our http connection in Python won't work right.

# This assignment was a little difficult. It involved combining several different things we had learned
# into one script. SQL is still something that I don't have much experience with, so it was good that the
# assignment included how to handle the SQL sections. I also took some time to decide how best to
# implement the functions. I also spent time deciding where/when to write the urls to the table. I first
# starting committing them to the table as they were found. Later, I decided to append the urls to a list
# and then committing them through a for loop that iterated through the list. 

# Code#

#####
# Adding scraped urls to table
# Code by AJChestnut
# 08-21-2020
#####

import http.client
import re
import sqlite3
from sqlite3 import Error
import datetime
import os


######
# function: create_table
# purpose: creates the storage table, if it doesn't already exist
# inputs: n/a
# returns: n/a
######
def create_table():
    try:
        curs.execute('CREATE TABLE IF NOT EXISTS storage(curtime TEXT, url TEXT)')
    except Error as e:
        print(e)
        exit(2)


######
# function: closeDB
# purpose: Close the database connection
# inputs: Nothing
# returns: Nothing
######
def closeDB(c):

    # Try to close the database connection
    try:
        c.close()
    except sqlite3.OperationalError as e:
        print(e)
        exit(5)


# Get directory
DIR_NAME = os.path.dirname(__file__)
try:
    db_path = os.path.join(DIR_NAME, "mydb.db")
except OSError as e:
    print(e)
    exit(0)


try:
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
except Error as e:
    print(e)
    exit(1)

create_table()


connection = http.client.HTTPSConnection("catalog.champlain.edu")
connection.request("GET", "/")

response = connection.getresponse()

count = 0
urls = []

while count < 500:  # Counter to limit time
    try:
        count = count + 1  # Increase counter each iteration
        line = response.readline()  # Read each line
        # Grab URL only
        u = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line.decode("utf-8"))
        if u:
            urls.append(str(u.group()))
        else:
            continue
    except KeyboardInterrupt as kI:
        print(kI)
        exit(4)

for url in urls:
    current_time = datetime.datetime.now().time()
    try:
        curs.execute('INSERT INTO storage (curtime, url) VALUES (?, ?)', (str(current_time), str(url)))
        conn.commit()
    except Error as e:
        print(e)
        exit(3)

closeDB(conn)
