import hashlib, os
import logging
import ICheckValidity
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror

class CheckIfUserValid(ICheckValidity.ICheckValidity):
    def __init__(self,mysql,email,password,data,result):
        self.mysql = mysql
        self.email =email
        self.password = password
        self.data = data
        self.result = result
        
    def emailIsValid(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if (self.data == ""):
                cur.callproc('spGetAllUsers')
                self.data = cur.fetchall()
                self.result = 'pass'
            conn.close()
        except Exception as e:
            excep_msg = "Error occured in emailIsValid method"
            self.result = 'fail'
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        self.data = list(self.data)
        for row in self.data:
            if row[0] == self.email and row[1] == hashlib.md5(self.password.encode()).hexdigest():
                return True
        return False
