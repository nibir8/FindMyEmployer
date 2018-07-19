import hashlib, os
import logging
import IFetchJobDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql


class Databaselayer_FetchJob(IFetchJobDetails.IFetchJobDetails):
    def getJob_DBL(self):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spFetchJobdetails')
            jobData = cur.fetchall()
        except:
            conn.rollback()
            excep_msg = "Error occured in getJob_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return jobData
