import os.path
import logging

import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_FetchUserData import Databaselayer_FetchUserData

class Businesslayer_FetchUserData:
    def getProfileData_BSL(Self,myemail):
        try:
            fetchuserdata = Databaselayer_FetchUserData()
            profileData = fetchuserdata.getProfileData_DBL(myemail)
            return profileData
        except:
            msg = "Error occured in method getProfileData_BSL method"
            logging.info(msg, exc_info=True)
