import os.path
import logging

import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from FetchSearchedProfile import FetchSearchedProfile

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror

class FetchMySearchedProfile:
    def __init__(self,firstName,finalMessage,fetchSearchedProfileData):
        self.firstName = firstName
        self.finalMessage = finalMessage
        self.fetchSearchedProfileData = fetchSearchedProfileData

    def set_messages(self,argument):
        return{
            'pass': 'Sucessfully fetched user records',
            'fail': 'Faliure in fetching in user records',
            '':'Faliure in fetching in user records'
        }[argument]

    def fetchMySearchedProfile(self):
        try:
            if self.finalMessage == "":
                fetchSearchedProfile = FetchSearchedProfile(mysql,self.firstName,'','')
                self.fetchSearchedProfileData,status = fetchSearchedProfile.fetchSearchedProfile()
                self.finalMessage = self.set_messages(status)
            return self.fetchSearchedProfileData,self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method fetchSearchedProfile_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
