import hashlib, os
import logging
import IFetchJobCount
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class FetchJobsCount(IFetchJobCount.IFetchJobCount):
    def __init__(self,mysql,email,JobsCount,result):
        self.mysql = mysql
        self.email = email
        self.JobsCount = JobsCount
        self.result = result


    def getJobsCount(self):
        try:
            conn = self.mysql .connect()
            cur = conn.cursor()
            if self.JobsCount == "":
                cur.callproc('spGetAllJobs',[self.email])
                self.JobsCount = len(cur.fetchall())
                self.result = "pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getJobsCount method"
            level = logging.getLogger().getEffectiveLevel()
            self.result = "fail"
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.JobsCount,self.result
