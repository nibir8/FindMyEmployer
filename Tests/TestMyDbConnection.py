from Test_Config import *

class TestCheckMyDbConnection(unittest.TestCase):
    def test_MyConnection(self):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.callproc('spGetAllUsers')
        count = len(cur.fetchall())
        if (count  >  0):
            value = "Connection Successfull"
        else:
            value = "Connection Unsuccessfull"

        assert value == "Connection Successfull"



if __name__ == "__main__":
    unittest.main()
