import hashlib, os
import logging
from extensions import mysql
import IFetchProfileDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql


class Databaselayer_FetchUserData(IFetchProfileDetails.IFetchProfileDetails):
    def getProfileData_DBL(Self,email):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetCompleteUserDetails',[email])
            profileData = cur.fetchone()
        except:
            conn.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return profileData
