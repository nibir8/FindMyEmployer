import sys, os
import os.path
import logging


sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_CheckIfUserValid import Databaselayer_CheckIfUserValid

class Businesslayer_CheckIfUserValid:
    def isValid_BSL(self,email, password):
        try:
            checkifuseremailisvalid = Databaselayer_CheckIfUserValid()
            value = checkifuseremailisvalid.isValid_DBL(email, password)
            return value
        except Exception as e:
            msg = "Error occured in method isValid_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(msg, exc_info=True)
