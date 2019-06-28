#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","123456","artgallery" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO customer(cid,
         cname, address, amount)
         VALUES ('2', 'praharsha','vskp', 50000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()