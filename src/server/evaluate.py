from database import *

class Evaluate:

    def __init__(self):
        pass

    #this command evaluates what the client wants and proceeds from there
    def read(self, msg):
        pre = msg.split(":")
        con = Database("test.db")
        tmp = con.query("SELECT name FROM tbl_users WHERE name == '%s'" % pre[1])
        if pre[0] == "login":
            if tmp is not None:
                return tmp[0]
                #this will be used if the user is logging in
                #need to connect to the database and check if the user exists
                #return "true"
            else:
                #returns as a guest user if the username does not exist
                #something random
                return "guest"

