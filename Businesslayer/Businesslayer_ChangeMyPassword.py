import os
import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_ChangeMyPassword import Databaselayer_ChangeMyPassword


class Businesslayer_ChangeMyPassword:
    def changeMyProfilePassword_BSL(Self,myemail,oldPassword,newPassword):
        try:
            changemypassword = Databaselayer_ChangeMyPassword()
            msg = changemypassword.changeMyProfilePassword_DBL(myemail,oldPassword,newPassword)
            return msg
        except:
            msg = "Error occured in method changeMyProfilePassword_BSL method"
            logging.info(msg, exc_info=True)
