#!/usr/bin/env python

from assign import *
from connect import *

con = Connect()
prompt = ">"

while 1:
    user = AssignValues()
    data = "login:" + user.name
    if con.send(data) == "true":
        #the user exists and he can start playing
        break
#they now reach a menu system that gives them a set of options

print '''
Welcome to Project Dolly!!!

Please feel free to have a look around
type help for more information
'''

#this is the menu system
while 1:
    print prompt,
    userin = raw_input()
    #if statements for every condition
    if userin == "q" or userin == "Q" or userin == "quit":
        break
    elif userin == "help":
        print "you have been helped"
    elif userin == "ls":
        print "you have 2 computers"
    else:
        print "command not found, type help for more information"


print "goodbye!"
