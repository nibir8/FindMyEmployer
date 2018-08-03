import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from LoginClass import LoginClass

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class LoginMyClass:
    def __init__(self,email,loggedIn, firstName, typeOfUser,value,result):
        self.email = email
        self.loggedIn = loggedIn
        self.firstName = firstName
        self.typeOfUser = typeOfUser
        self.value = value
        self.result = result
	
    def getMyLoginDetails(self):
        try:
            if (self.value == ''):
                getlogindetails = LoginClass(mysql,self.email,'', '', '', '')
                self.loggedIn, self.firstName, self.typeOfUser = getlogindetails.getLoginDetails()
                return (self.loggedIn, self.firstName, self.typeOfUser)
        except Exception as e:
            excep_msg = "Error occured in method getMyLoginDetails method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
