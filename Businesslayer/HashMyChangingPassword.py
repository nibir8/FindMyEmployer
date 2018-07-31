import os
import os.path
import logging
import sys
import hashlib

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from ChangeMyPassword import ChangeMyPassword
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class HashMyChangingPassword:
    def __init__(self,myemail,oldPassword,newPassword,msg):
        self.myemail = myemail
        self.oldPassword =oldPassword
        self.newPassword = newPassword
        self.finalMessage = msg

    def set_messages(self,argument):
        return{
            'pass': 'Password Updated Successfully',
            'fail': 'Invalid password'
        }.get(argument, 'Invalid password')

    def hashMyChangingPassword(self):
        try:
            self.oldPassword = hashlib.md5(self.oldPassword.encode()).hexdigest()
            self.newPassword = hashlib.md5(self.newPassword.encode()).hexdigest()
            if self.finalMessage == "":
                changemypassword = ChangeMyPassword(self.myemail,self.oldPassword,self.newPassword,mysql,'')
                status = changemypassword.changeMyProfilePassword()
                self.finalMessage = self.set_messages(status)
            return self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method HashMyChangingPassword businesslayer"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
