import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_GetUserType import Databaselayer_GetUserType

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_GetUserType:
    def getUserType_BSL(self,email):
        try:
            getUserType = Databaselayer_GetUserType()
            getUserTypeData = getUserType.getUserType_DBL(email)
            return getUserTypeData
        except Exception as e:
            excep_msg = "Error occured in method getUserType_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
