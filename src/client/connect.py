import httplib
import sys

class Connect:

    def __init__(self, http_server="127.0.0.1",port=5000):
        self.http_server = http_server
        self.port = port

    def send(self, msg):
        #get http server ip
        #create a connection
        conn = httplib.HTTPConnection(self.http_server, self.port)

        #request command to server
        conn.request("GET", msg)

        #get response from server
        rsp = conn.getresponse()

        #print server response and data
        #print(rsp.status, rsp.reason)
        data_received = rsp.read()
            
        conn.close()

        return data_received
