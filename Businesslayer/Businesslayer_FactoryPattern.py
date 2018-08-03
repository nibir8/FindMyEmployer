import os
import os.path
import logging
import sys
from Businesslayer import Email_NullCheck
from Businesslayer import Password_NullCheck
from Businesslayer import Businesslayer_Validator_Email_Validate
from Businesslayer import Businesslayer_Validator_FirstName_SpaceCheck
from Businesslayer import Password_Equate
from Businesslayer import Password_SpaceCheck

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror


class Businesslayer_FactoryPattern:
    @staticmethod
    def factoryPattern_BSL(validatorName):
        try:
            if (validatorName == 'Email NullCheck'):
                return Email_NullCheck.Email_NullCheck()
            if (validatorName == 'Email Validate'):
                return Businesslayer_Validator_Email_Validate.Businesslayer_Email_Validate()
            if (validatorName == 'FirstName SpaceCheck'):
                return Businesslayer_Validator_FirstName_SpaceCheck.Businesslayer_FirstName_SpaceCheck()
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