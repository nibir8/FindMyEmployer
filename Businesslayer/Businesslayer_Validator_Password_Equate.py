import os
import os.path
import logging
import sys
import IPasswordEquate

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_Password_Equate(IPasswordEquate.IPasswordEquate):
    def Businesslayer_Password_Equate_BSL(self,password1,password2):
        try:
            if (password1 == password2):
                return password1
            else:
                return "Two Passwords do not match"
        except Exception as e:
            excep_msg = "Error occured in method Businesslayer_Password_Equate_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)