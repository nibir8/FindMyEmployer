import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_LoginClass import Databaselayer_LoginClass


class Businesslayer_LoginClass:
    def getLoginDetails_BSL(self,myemail):
        try:
            getlogindetails = Databaselayer_LoginClass()
            loggedIn, firstName = getlogindetails.getLoginDetails_DBL(myemail)
            return (loggedIn, firstName)
        except:
            msg = "Error occured in method getLoginDetails_BSL method"
            logging.info(msg, exc_info=True)
