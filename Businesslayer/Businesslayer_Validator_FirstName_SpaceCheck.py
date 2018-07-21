import os
import os.path
import logging
import sys
import IOnlySpaceCheck

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_FirstName_SpaceCheck(IOnlySpaceCheck.IOnlySpaceCheck):
    def Businesslayer_FirstName_SpaceCheck_BSL(self,firstName):
        try:
            if (firstName.isspace() == True):
                return "Firstname not valid"
            else:
                return firstName
        except Exception as e:
            excep_msg = "Error occured in method Businesslayer_FirstName_SpaceCheck_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)