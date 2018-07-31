import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from InsertMyJob import InsertMyJob

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensions import mysql

class InsertUserJob:
    def __init__(self,jobId,companyName,title,manager,location,jobDetails,email,msg):
        self.jobId = jobId
        self.companyName =companyName
        self.title = title
        self.manager = manager
        self.location = location
        self.jobDetails = jobDetails
        self.email = email
        self.msg = msg

    def set_messages(self,argument):
        return{
            'pass': 'Added Job Successfully',
            'fail': 'Could not add job',
            '':'Unable to add job'
        }.get(argument, 'Could not add job')


    def insertUserJob(self):
        try:
            if self.msg == "":
                insertjob = InsertMyJob(mysql,self.jobId,self.companyName,self.title,self.manager,self.location,self.jobDetails,self.email,'')
                result = insertjob.insertMyJob()
                self.msg = self.set_messages(result)
        except Exception as e:
            excep_msg = "Error occured in method insertUserJob method"
            self.msg = "Unable to add job"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        return self.msg
