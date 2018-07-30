from flask import Flask
from flaskext.mysql import MySQL
import unittest
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'CSCI5308_15_DEVINT_USER'
app.config['MYSQL_DATABASE_PASSWORD'] = 'CSCI5308_15_DEVINT_15142'
app.config['MYSQL_DATABASE_DB'] = 'CSCI5308_15_DEVINT'
app.config['MYSQL_DATABASE_HOST'] = 'db-5308.cs.dal.ca'

mysql.init_app(app)

class TestCheckMyDbConnection(unittest.TestCase):
    def test_MyConnection(self):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.callproc('spGetAllUsers')
        count = len(cur.fetchall())
        if (count  >  0):
            value = "ConnectionSuccessfull"
        else:
            value = "Connection Unsuccessfull"

        assert value == "ConnectionSuccessfull"



if __name__ == "__main__":
    unittest.main()
