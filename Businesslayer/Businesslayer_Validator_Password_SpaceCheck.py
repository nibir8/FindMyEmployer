import os
import os.path
import logging
import sys
import IOnlySpaceCheck

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_Password_SpaceCheck(IOnlySpaceCheck.IOnlySpaceCheck):
    def Businesslayer_Password_SpaceCheck_BSL(self,password):
        try:
            if (password.isspace() == True):
                return "Password not valid"
            else:
                return password
        except Exception as e:
            excep_msg = "Error occured in method Businesslayer_Password_SpaceCheck_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)