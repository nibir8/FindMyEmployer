import hashlib, os
import logging
from extensions import mysql
import IFetchSearchedProfile
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class FetchSearchedProfile(IFetchSearchedProfile.IFetchSearchedProfile):
    def __init__(self,mysql,firstName,fetchSearchedProfileData,result):
        self.mysql = mysql
        self.firstName = firstName
        self.fetchSearchedProfileData = fetchSearchedProfileData
        self.result = result


    def fetchSearchedProfile(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spGetSearchedUser',[self.firstName])
                self.fetchSearchedProfileData = cur.fetchall()
                self.result = "pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in fetchSearchedProfile_DBL method"
            self.result = "fail"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.fetchSearchedProfileData,self.result
