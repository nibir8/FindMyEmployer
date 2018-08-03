import os
import os.path
import logging
import sys
from Businesslayer import Email_NullCheck
from Businesslayer import Password_NullCheck
from Businesslayer import Email_Validate
from Businesslayer import FirstName_SpaceCheck
from Businesslayer import Password_Equate
from Businesslayer import Password_SpaceCheck

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror


class FactoryPattern:
    @staticmethod
    def factoryPattern(validatorName):
        try:
            if (validatorName == 'Email NullCheck'):
                return Email_NullCheck.Email_NullCheck()
            if (validatorName == 'Email Validate'):
                return Email_Validate.Email_Validate()
            if (validatorName == 'FirstName SpaceCheck'):
                return FirstName_SpaceCheck.FirstName_SpaceCheck()
            if (validatorName == 'Password NullCheck'):
                return Password_NullCheck.Password_NullCheck()
            if (validatorName == 'Password Equate'):
                return Password_Equate.Password_Equate()
            if (validatorName == 'Password SpaceCheck'):
                return Password_SpaceCheck.Password_SpaceCheck()
        except Exception as e:
            excep_msg = "Error occured in method factoryPattern_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
