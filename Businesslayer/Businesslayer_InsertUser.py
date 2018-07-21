import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_InsertUser import Databaselayer_InsertUser

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

sys.path.append(os.path.abspath(os.path.join('0', '../models')))
from User import User

class Businesslayer_InsertUser:
    def insertNewUser_BSL(self,myuser):
        try:
            insertuser = Databaselayer_InsertUser()
            print myuser.firstName
            insertuser.insertNewUser_DBL(myuser)
        except Exception as e:
            excep_msg = "Error occured in method insertNewUser_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
