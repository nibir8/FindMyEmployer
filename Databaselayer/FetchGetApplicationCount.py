import hashlib, os
import logging
import IFetchApplicationDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class FetchGetApplicationCount(IFetchApplicationDetails.IFetchApplicationDetails):
    def __init__(self,mysql,email,applicationCount,result):
        self.mysql = mysql
        self.email = email
        self.applicationCount = applicationCount
        self.result = result

    def getApplicationCount(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.applicationCount == "":
                cur.callproc('spGetUserApplications',[self.email])
                self.applicationCount = len(cur.fetchall())
                self.result='pass'
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getApplicationCount_DBL method"
            self.result='fail'
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.applicationCount,self.result
