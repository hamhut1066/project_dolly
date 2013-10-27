class Menu:
    def __init__(self):
        pass

    def helper_menu(self):
        while 1:
            print """ 
                    welcome to the helper menu!
                    1: help with [l]ogin
                    2:help with [g]ameplay
                    3:help with s[o]mething else"
                    """
            choice = raw_input( "give your choice: "), 

            if choice[0] == "l":
                print "you have been helped with login"
            elif choice[0] == "g": 
                print "you have been helped with gameplay "
            elif choice[0] == "o":
                print "you have been helped with something else "
            elif choice[0] == "q" or choice[0] == "b":
                break
            print "...",
            raw_input()
