import hashlib, os
import logging
from extensions import mysql
import IPostStatus
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class PostMyStatus(IPostStatus.IPostStatus):
    def __init__(self,mysql,email,status,msg):
        self.mysql = mysql
        self.email = email
        self.status = status
        self.result = msg

    def insertMyUserStatus(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spInsertUserStatus',[self.email,self.status])
                conn.commit()
                self.result ="pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            self.result ="fall"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.result
