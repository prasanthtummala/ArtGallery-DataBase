import pymysql

# Open database connection
db = pymysql.connect("localhost","root","123456","artgallery" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM  "
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:

      MNAME = row[0]
      gross = row[1]

      # Now print fetched result
      print ("{0} {1} ".format(MNAME,gross))
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()