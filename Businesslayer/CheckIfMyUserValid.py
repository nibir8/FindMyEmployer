import sys, os
import os.path
import logging


sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from CheckIfUserValid import CheckIfUserValid
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror

class CheckIfMyUserValid:
    def __init__(self,email,password,value,result):
        self.email =email
        self.password = password
        self.value = value
        self.result = result
		
    def isValid(self):
        try:
            if (self.value == ''):
                checkifuseremailisvalid = CheckIfUserValid(mysql,self.email,self.password,'','')
                self.value = checkifuseremailisvalid.emailIsValid()
            if self.value == False:
                self.result = 'Invalid UserId / Password'
                return self.result
            elif self.value == True:
                return self.value
        except Exception as e:
            excep_msg = "Error occured in method isValid method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
