import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from GetUserType import GetUserType
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensions import mysql


class GetMyUserType:
    def __init__(self,myemail,userTypeData,finalMessage):
        self.myemail = myemail
        self.userTypeData =userTypeData
        self.finalMessage = finalMessage

    def set_messages(self,argument):
        return{
            'pass': 'Fetched usertype sucessfully',
            'fail': 'Unable to fetch usertype',
            '':'Unable to fetch user type'
        }[argument]



    def getMyUserType(self):
        try:
            if self.finalMessage == "":
                getUserType = GetUserType(mysql,self.myemail,'','')
                self.userTypeData,status = getUserType.getUserType()
                self.finalMessage = self.set_messages(status)
            return self.userTypeData,self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method getMyUserType method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
