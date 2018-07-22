import os
import os.path
import logging
import sys
import INullChecker

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_Email_NullCheck(INullChecker.INullChecker):
    def Businesslayer_Email_NullCheck_BSL(self,email):
        try:
            if (email == ""):
                error = 'Dont leave userId/Password blank'
                return error
        except Exception as e:
            excep_msg = "Error occured in method Businesslayer_Email_NullCheck_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)