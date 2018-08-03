import os.path
import logging
import sys
from UpdateMyUserobject import UpdateMyUserobject
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from FetchUserData import FetchUserData

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensionsUser import myUser
from extensions import mysql

class FetchMyUserData:
    def __init__(self,email,profileData,finalMessage):
        self.email = email
        self.profileData = profileData
        self.finalMessage = finalMessage

    def set_messages(self,argument):
        return{
            'pass': 'Fetched user data sucessfully',
            'fail': 'Unable to fetch user data',
            '':'Unable to fetch user data'
        }[argument]

    def getMyProfileData(self):
        try:
            if self.finalMessage == "":
                fetchuserdata = FetchUserData(mysql,self.email,'','')
                self.profileData,status = fetchuserdata.getProfileData()
                profileData_list = self.profileData
                profileData_list = list(profileData_list)
                user_details_list = profileData_list[11:33]
                updateMyobject = UpdateMyUserobject(self.profileData[1],self.profileData[2],self.profileData[3],self.profileData[4],self.profileData[5],self.profileData[6],self.profileData[7],self.profileData[8],self.profileData[9],self.profileData[10],user_details_list,self.profileData[34],self.profileData[35])
                myuser = updateMyobject.updateMyObject()
                self.finalMessage = self.set_messages(status)
            return self.profileData,self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method getMyProfileData method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
