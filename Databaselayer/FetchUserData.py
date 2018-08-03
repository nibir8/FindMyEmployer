import hashlib, os
import logging
from extensions import mysql
import IFetchProfileDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class FetchUserData(IFetchProfileDetails.IFetchProfileDetails):
    def __init__(self,mysql,email,profileData,result):
        self.mysql = mysql
        self.email = email
        self.profileData = profileData
        self.result = result

    def getProfileData(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spGetCompleteUserDetails',[self.email])
                self.profileData = cur.fetchone()
                self.result="pass"
        except Exception as e:
            conn.rollback()
            self.result="fail"
            excep_msg = "Error occured in getProfileData method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.profileData,self.result
