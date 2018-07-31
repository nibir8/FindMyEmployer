import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from InsertMyJobApplication import InsertMyJobApplication

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensions import mysql

class InsertGivenJobApplication:
    def __init__(self,email,msg):
        self.email = email
        self.finalMessage = msg

    def set_messages(self,argument):
        return{
            'pass': 'Successfully submitted application',
            'fail': 'Unable to submit the application'
        }.get(argument, 'Unable to submit the application')

    def insertGivenJobApplication(self):
        try:
            if self.finalMessage == "":
                insertjobApplication = InsertMyJobApplication(mysql,self.email,'')
                result = insertjobApplication.insertMyJobApplication()
                self.finalMessage = self.set_messages(result)
            return self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method InsertJobApplication method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
