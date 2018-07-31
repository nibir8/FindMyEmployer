import hashlib, os
import logging
from extensions import mysql
import IInsertJobDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror



class InsertMyJob(IInsertJobDetails.IInsertJobDetails):
    def __init__(self,mysql,jobId,companyName,title,manager,location,jobDetails,emailid,result):
        self.mysql = mysql
        self.jobId = jobId
        self.companyName = companyName
        self.title = title
        self.manager = manager
        self.location = location
        self.jobDetails = jobDetails
        self.emailid = emailid
        self.result = result

    def insertMyJob(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result =="":
                cur.callproc('spInsertJobDetails',[self.jobId,self.companyName,self.title,self.manager,self.location,self.jobDetails,self.emailid])
                conn.commit()
                self.result = "pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in insertMyJob method"
            self.result = "fail"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.result
