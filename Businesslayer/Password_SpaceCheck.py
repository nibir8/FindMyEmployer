import os
import os.path
import logging
import sys
import IValidator

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Password_SpaceCheck(IValidator.IValidator):
    def formValidate_BSL(self,password):
        try:
            if (password.isspace() == True):
                return "Password not valid"
            else:
                return password
        except Exception as e:
            excep_msg = "Error occured in method formValidate_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)