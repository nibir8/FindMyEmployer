import hashlib, os
import logging
import IFetchUserType
import sys

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class GetUserType(IFetchUserType.IFetchUserType):
    def __init__(self,mysql,myemail,userTypeData,result):
        self.mysql = mysql
        self.myemail = myemail
        self.userTypeData =userTypeData
        self.result = result

    def getUserType(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spGetUserDetails',[self.myemail])
                self.userTypeData = cur.fetchone()
                self.result = "pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getUserType method"
            self.result = "fail"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.userTypeData,self.result
