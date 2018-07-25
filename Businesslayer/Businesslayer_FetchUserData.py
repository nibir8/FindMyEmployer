import os.path
import logging
import sys

from Businesslayer import Businesslayer_UpdateMyobject
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_FetchUserData import Databaselayer_FetchUserData

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensionsUser import myUser

class Businesslayer_FetchUserData:
    def getProfileData_BSL(Self,myemail):
        try:
            fetchuserdata = Databaselayer_FetchUserData()
            profileData = fetchuserdata.getProfileData_DBL(myemail)
            profileData_list = profileData
            profileData_list = list(profileData_list)
            user_details_list = profileData_list[11:33]
            updateMyobject = Businesslayer_UpdateMyobject()
            updateMyobject.updateMyObjectBSL(profileData[1],profileData[2],profileData[3],profileData[4],profileData[5],profileData[6],profileData[7],profileData[8],profileData[9],profileData[10],user_details_list,profileData[34],profileData[35])
            return profileData
        except Exception as e:
            excep_msg = "Error occured in method getProfileData_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
