import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_InsertJobApplication import Databaselayer_InsertJobApplication

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_InsertJobApplication:
    def insertJobApplication_BSL(self,email):
        try:
            insertjobApplication = Databaselayer_InsertJobApplication()
            msg = insertjobApplication.insertJobApplication_DBL(email)
        except Exception as e:
            excep_msg = "Error occured in method insertJobApplication_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        return msg
