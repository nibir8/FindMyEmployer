import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_InsertUser import Databaselayer_InsertUser

class Businesslayer_InsertUser:
    def insertNewUser_BSL(self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType):
        try:
            insertuser = Databaselayer_InsertUser()
            insertuser.insertNewUser_DBL(password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType)
        except Exception as e:
            msg = "Error occured in method insertNewUser_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(msg, exc_info=True)
