
class Evaluate:

    def __init__(self):
        pass

    #this command evaluates what the client wants and proceeds from there
    def read(self, msg):
        pre = msg.split(":")
        if pre[0] == "login" and pre[1] == "aoeu":
            #this will be used if the user is logging in
            return "true"
        else:
            #this will check that the user is logging in otherwise it will do
            #something random
            return pre
