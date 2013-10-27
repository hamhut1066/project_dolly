#import user
#import computer
#import port
from connect import *

class AssignValues:
    name = ""

    def __init__(self):
        self.assign_user()

    def assign_user(self):
        print "username:",
        self.name = raw_input()


    def assign_computer (self,computer,check_compadd): #check_compadd returns the number of computer a user can add
        if (check_compadd == 0):
            pass
        else:
            assign_computer = input ( "enter computer name")
            check_compadd = check_compadd -1




    def assign_port(self, ports,check_portadd): #check_portadd checks the number of ports a user can add
        if (check_portadd == 0):
            pass
        else:
            assign_port = input ( "enter computer name")
            check_portadd = check_portadd -1
