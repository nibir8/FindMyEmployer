import os
import os.path
import logging
import sys
import IEmailValidator
import re

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_Email_Validate(IEmailValidator.IEmailValidator):
    def Businesslayer_Email_Validate_BSL(self,email):
        try:
            regex_emailCheck = re.compile("^\S+@\S+$")
            if (regex_emailCheck.match(email)):
                return email
            else:
                msg = "Email address not valid"
                return msg
        except Exception as e:
            excep_msg = "Error occured in method Businesslayer_Email_Validate_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)