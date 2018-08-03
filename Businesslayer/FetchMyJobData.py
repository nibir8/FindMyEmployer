import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from FetchJobData import FetchJobData
from extensions import mysql

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class FetchMyJobData:
    def __init__(self,jobData,finalMessage):
        self.jobData =jobData
        self.finalMessage = finalMessage

    def set_messages(self,argument):
        return{
            'pass': 'Job fetched successfully',
            'fail': 'Unable to fetch job details',
            '':'Unable to fetch job details'
        }[argument]


    def getMyJobData(self):
        try:
            if self.finalMessage == "":
                fetchjobdata = FetchJobData(mysql,'','')
                self.jobData,status = fetchjobdata.getJobData()
                self.finalMessage = self.set_messages(status)
            return self.jobData,self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method getMyJobData method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
