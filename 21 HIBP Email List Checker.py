#Assignment 21:

# You will be working on designing and developing this program through the entire course. The program 
# you turn in needs to match the final design document you submit and have been working on during the 
# term. Functionality in the final design document needs to be in your final project. All of the 
# documentation standards will be in play here, just as they have been in the weekly programming 
# assignments.

# Your assignment will be graded on the following:

# Completeness: Does it do what you designed it to do according to your FINAL design document.
# In other words, if you change things throughout the course, update your Final Design Document to 
# incorporate your changes.
# It would ideally solve some security related problem but if you have some purpose that a 
# Python program can help you solve that is not entirely security related, as long as you pertain
# to at least the next requirements you should be fine.
# Your program contains some networking element.  This includes but is not limited to:
#   Client/Host communication
#   Port scanning
#   Network tracing
#   Some form of Web Site Spidering/connecting
#   Emailing some content through external email server
#   Logging into some remote system view telnet/ssh
# Your program should have some file interaction, which should include EITHER input from a file 
# (e.g., database), or output to a file (e.g., database, XML, text file, etc).

# This assignemnt was the final project for the class. We started with creating the design document
# for our idea. As, we progressed through the class, we would update the design document as we went. 
# If something became clear that it was out of scope, we would remove it. If we found something that 
# we wanted to add, we could add it in. As long as your project met the requirements, anything else
# you decided to do was extra. It added a lot of flexibility for the project. 

# I decided to write a script that would read a list of emails from a text file, send them to the 
# HaveIBeenPwned.com API, then write the response to a different file. From my research, I couldn't
# find a way to poll the HIBP for all emails ending in the same domain, i.e., "@companyname.com." 
# So, to check all of a company's emails, you would have to poll each one individually. 

# This project appealed to me because I have always been impressed with what Troy Hunt has 
# accomplished with HaveIBeenPwned, and it also was a bit of automation that would speed up the 
# process of checking a list of company email addresses, which I thought would be usful.

# This was my first time working with an API. Ensuring that I had all of the elements that
# the API required and in the proper formatting, took some trial and error. It was also
# a little bit worrysome that I was interacting with someone else's system. All of my
# projects up to this point had been selfcontained or only interacted with my school's website. 
# Making a mistake that could negtively effect someone's else system was always in the back
# of my mind. I was sure that the HIBP API was setup in a way that I wouldn't be able to 
# unintentionally hurt it, but it was still something I wanted to be aware of.

# For this script to work, it requires 3 .txt files in the same directory as the script:
# emails.txt, which is a list of the emails you want to check, each email on their own line
# breaches.txt, which is an empty txt file.
# APIKey.txt, which is a text file containing the API key, to avoid having to hard code it.

#####
# HIBP API Email Checker
# Code by AJChestnut
# 08-21-2020
# Read emails from a list, checks against the HaveIBeenPwned database, writes results to a text file


import http.client
import time
import json

######
# function: breach_found
# purpose: adds the breach data to a text file if breach is found
# inputs: breached email, breach data
# returns: n/a
######
def breach_found(x, y):
    try:
        f = open('breaches.txt', 'a')
        f.write(x + '\n' + str(y) + '\n')
        f.close()
    except IOError as e:
        print('There was a problem writing found to the breaches file: ' + e)
        exit(0)

######
# function: breach_notfound
# purpose: If no breach is found, updates text file to reflect
# inputs: checked email
# returns: n/a
######
def breach_notfound(x):
    try:
        f = open('breaches.txt', 'a')
        f.write(a + '\n' + 'No breaches found at this time.' + '\n')
        f.close()
    except IOError as e:
        print('There was a problem writing not found to the breaches file: ' + e)
        exit(0)

try:
    with open('APIKey.txt', 'r') as f:
        apiKey = f.read()

except IOError as e:
    print('There was a problem opening the apiKey file: ' + e)
    exit(0)

#  headers required by the API
headers = {'user-agent':'python-script',
           'hibp-api-key':apiKey}



#  try block of opening the text file and reading each line into a list
try:
    with open('emails.txt', 'r') as f:
        emails = f.readlines()
    emails = [x.strip() for x in emails]    # strip out the whitespace characters
except IOError as e:
    print('There was a problem opening the emails file: ' + e)
    exit(0)

#  loop through the email addresses
for a in emails:
    time.sleep(2)   # respect the rate limit of 1 request per 1.5 seconds by API

    domain = 'haveibeenpwned.com' #  the domain of the api
    api_url = ('/api/v3/breachedaccount/%s') % (str(a))    # api call for each email
    connection = http.client.HTTPSConnection(domain)
    connection.request('GET', 'https://' + domain + api_url,'',headers)
    response = connection.getresponse()
    status = response.status
    if status == 200:    # HTTP status 200 is returned if a breach is found
        content = response.read()    # read the json response
        breaches = json.loads(content)    # convert json to python object
        # write the returned breaches to the breaches text file
        breach_found(a, breaches)

    elif status == 404:    # HTTP status 404 is returned if no breach is found
        # update breaches text file stating that no breaches were found for this address
        breach_notfound(a)

print('The Breaches file has been updated.') # I like confirmation messages
