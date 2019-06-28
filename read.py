#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","123456","artgallery")
# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM customer"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
       cname = row[0]
       cid = row[1]
       address = row[2]
       amount = row[3]

      # Now print fetched result
      print ("cname=%s,cid=%s,address=%d,amount=%s")
except:
   print("Error: unable to fecth data")

# disconnect from server
db.close()