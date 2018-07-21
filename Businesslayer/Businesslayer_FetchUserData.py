import os.path
import logging

import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_FetchUserData import Databaselayer_FetchUserData

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_FetchUserData:
    def getProfileData_BSL(Self,myemail):
        try:
            fetchuserdata = Databaselayer_FetchUserData()
            profileData = fetchuserdata.getProfileData_DBL(myemail)
            if (not profileData):
                return profileData
            else:
                msg = "Email ID already exists"
                return msg
        except Exception as e:
            excep_msg = "Error occured in method getProfileData_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
