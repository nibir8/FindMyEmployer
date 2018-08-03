import hashlib, os
import logging
from extensions import mysql
import IFetchLoginDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class LoginClass(IFetchLoginDetails.IFetchLoginDetails):
    def __init__(self,mysql,email,userId, firstName, typeOfUser,result):
        self.mysql = mysql
        self.email = email
        self.userId = userId
        self.firstName = firstName
        self.typeOfUser = typeOfUser
        self.result = result
	
    def getLoginDetails(self):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            loggedIn = False
            if ((self.userId == "")and(self.firstName == "")and(self.typeOfUser == "")):
                cur.callproc('spGetUserDetails',[self.email])
                self.userId, self.firstName, self.typeOfUser = cur.fetchone()
                loggedIn = True
                self.result = 'pass'
        except Exception as e:
            excep_msg = "Error occured in getLoginDetails method"
            self.result = 'fail'
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return (loggedIn, self.firstName,self.typeOfUser)

		