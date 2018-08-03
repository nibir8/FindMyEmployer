import hashlib, os
import logging
import IFetchJobDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class FetchJobData(IFetchJobDetails.IFetchJobDetails):
    def __init__(self,mysql,jobData,result):
        self.mysql = mysql
        self.jobData =jobData
        self.result = result


    def getJobData(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spFetchJobdetails')
                self.jobData = cur.fetchall()
                self.result = "pass"
        except Exception as e:
            conn.rollback()
            self.result = "fail"
            excep_msg = "Error occured in getJobData method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.jobData,self.result
