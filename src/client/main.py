#!/usr/bin/env python

from assign import *
from connect import *
from menu import *

con = Connect()
prompt = ">"
username = "guest"

while 1:
    user = AssignValues()
    data = "login:" + user.name
    username = con.send(data)
    if username != "guest":
        #the user exists and he can start playing
        break
    print return_val
#they now reach a menu system that gives them a set of options

print '''
Welcome %s, to Project Dolly!!!

Please feel free to have a look around.
type [h]elp for more information
''' % username
men = Menu()
functions = {
        'h'    : men.helper_menu,
        'H'    : men.helper_menu,
        'help' : men.helper_menu,
        'ls'   : men.helper_menu
        }
#this is the menu system
while 1:
    print prompt,
    userin = raw_input()
    #if statement to quit the game if needed
    if userin == "q" or userin == "Q" or userin == "quit":
        break
    #a dictionary of functions to call depending on user input
    else:
        #using try-catch to stop invalid options from crashing the program
        try:
            func = functions[userin]
            func()
        except:
            print "Command not Found, type h for help"


print "goodbye!"
