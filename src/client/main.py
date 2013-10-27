#!/usr/bin/env python

from assign import *
from connect import *

con = Connect()
user = AssignValues()

data = "username:" + user.name
print data
print con.send(data)
