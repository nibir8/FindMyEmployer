import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_PostStatus import Databaselayer_PostStatus

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_PostStatus:
    def insertUserStatus_BSL(Self,email,status):
        try:
            databaselayerupdatestatus = Databaselayer_PostStatus()
            databaselayerupdatestatus.insertUserStatus_DBL(email,status)
        except Exception as e:
            excep_msg = "Error occured in method insertUserStatus_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
