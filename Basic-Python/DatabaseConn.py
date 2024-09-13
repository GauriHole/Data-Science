# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:32:47 2024

@author: Lenovo
"""

import psycopg2 as pg2

#Create a connection with PostgreSql
#Password is whatever password you set, we set password in the install 
conn = pg2.connect(database='dvdrental', user='postgres', password='root')
cur =  conn.cursor()
cur.execute("SELECT * from payment")
#pass in a postgreSQL query as astring
cur.fetchone()
#return a tuple of the first row as python object

cur.fetchmany(10)
#Return N number of rows

cur.fetchall()
#Return All rows at once

data = cur.fetchmany(10)
#To save and index results, assign it to a variable

conn.close()
