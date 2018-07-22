import hashlib, os
import logging
import IFetchJobCount
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class Databaselayer_FetchJobsCount(IFetchJobCount.IFetchJobCount):
    def getJobsCount_DBL(self,email):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetAllJobs',[email])
            JobsCount = len(cur.fetchall())
            print JobsCount
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getJobsCount_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return JobsCount
