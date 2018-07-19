import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_LoginClass import Databaselayer_LoginClass

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror


class Businesslayer_LoginClass:
    def getLoginDetails_BSL(self,myemail):
        try:
            getlogindetails = Databaselayer_LoginClass()
            loggedIn, firstName = getlogindetails.getLoginDetails_DBL(myemail)
            return (loggedIn, firstName)
        except Exception as e:
            excep_msg = "Error occured in method getLoginDetails_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
