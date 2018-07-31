import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from FetchUserStatuses import FetchUserStatuses

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror

class FetchAllUserStatuses:
    def __init__(self,StatusData,msg):
        self.finalMessage = msg
        self.StatusData = StatusData

    def set_messages(self,argument):
        return{
            'pass': 'User Staus Fetched Successfully',
            'fail': 'Unable to fetch user status'
        }.get(argument, 'Unable to fetch user status')

    def getAllUserStatus(self):
        try:
            if self.finalMessage == "":
                fetchuserStatus = FetchUserStatuses(mysql,self.StatusData,'')
                self.StatusData,result  = fetchuserStatus.getUserStatuses()
                self.finalMessage = self.set_messages(result)
            return self.StatusData,self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method getAllUserStatus in businesslayer"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
