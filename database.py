import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table for users
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')
		
#Create table for jobs
conn. execute('''CREATE TABLE jobs
         (jobId INTEGER PRIMARY KEY,
		 companyName TEXT,
		 title TEXT,
         manager TEXT,
		 location TEXT,
		 jobDetails TEXT
		 )''')
		 
conn.close()