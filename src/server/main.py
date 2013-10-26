#!/usr/bin/python2


import database

meh = database.Database()


a = meh.query("SELECT * from cars")

print(a[1])
