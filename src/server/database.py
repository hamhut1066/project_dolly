#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

class Database:

    def __init__(self, db="test.db"):
        self.db = db





    def connect(self):
        con = lite.connect(self.db)
        with con:

            #connect to database
            return con.cursor()    
            #cur.execute('SELECT SQLITE_VERSION()')

            #data = cur.fetchone()

    def query(self, string=""):
        cur = self.connect()
        cur.execute(string)
        return cur.fetchone()

    def update(self, string=""):
        cur = self.connect()
        cur.execute(string)
        return cur.fetchone()
