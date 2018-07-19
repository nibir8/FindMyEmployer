import os
import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_ChangeMyPassword import Databaselayer_ChangeMyPassword
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror


class Businesslayer_ChangeMyPassword:
    def changeMyProfilePassword_BSL(Self,myemail,oldPassword,newPassword):
        try:
            changemypassword = Databaselayer_ChangeMyPassword()
            msg = changemypassword.changeMyProfilePassword_DBL(myemail,oldPassword,newPassword)
            return msg
        except Exception as e:
            excep_msg = "Error occured in method changeMyProfilePassword_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
