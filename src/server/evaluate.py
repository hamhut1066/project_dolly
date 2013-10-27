
class Evaluate:

    def __init__(self):
        pass

    def read(self, msg):
        pre = msg.split(":")
        if pre[0] == "username":
            return "login"
        else:
            return 
