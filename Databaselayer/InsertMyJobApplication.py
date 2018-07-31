import hashlib, os
import logging
from extensions import mysql
import IInsertJobApplication
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror

class InsertMyJobApplication(IInsertJobApplication.IInsertJobApplication):
    def __init__(self,mysql,email,msg):
        self.mysql = mysql
        self.email = email
        self.result = msg

    def insertMyJobApplication(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spInsertJobApplication',[self.email])
                conn.commit()
                self.result = "pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in insertMyJobApplication method"
            self.result = "fail"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.result
