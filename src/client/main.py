#!/usr/bin/env python

import httplib
import sys

class Test:

    a = ""
    def __init__(self):
        self.a = "hello"

    def __getitem__(self):
        return self.a

#get http server ip
http_server = "127.0.0.1"
port = 5000
#create a connection
conn = httplib.HTTPConnection(http_server, port)

i = 0
while i < 10:
    i+=1
    #this can be changed to take user input
    cmd = Test()

    #request command to server
    conn.request("GET", cmd.a)

    #get response from server
    rsp = conn.getresponse()
    
    #print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)
    
conn.close()
