import os
import unittest
import sqlite3
import unittest
import tempfile
import hashlib

class FlasApp(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
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
        cursor.execute("INSERT INTO users VALUES "
                       "( 1, '123', 'rohit.gs28@gmail.com',"
                       "'Rohit', 'Gollarahalli','#1333 South park street','Suite no 2108','B3J2K9','Halifax','NS','Canada','9008491493')")
        conn.commit()
        conn.close()

    def deleteDatabase(self):
        os.remove("database.db")


if __name__ == '__main__':
    unittest.main()
