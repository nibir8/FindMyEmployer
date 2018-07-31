import hashlib, os
import logging
import IPasswordUpdate
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class ChangeMyPassword(IPasswordUpdate.IPasswordUpdate):
    def __init__(self,myemail,oldPassword,newPassword,mysql,msg):
        self.myemail = myemail
        self.oldPassword =oldPassword
        self.newPassword = newPassword
        self.mysql = mysql
        self.result = msg

    def changeMyProfilePassword(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spFetchUserPassword',[self.myemail])
                userId, password = cur.fetchone()
                if (password == self.oldPassword):
                    cur.callproc('spUpdatePassword',[self.newPassword,userId])
                    conn.commit()
                    msg="pass"
                else:
                    msg = "fail"
                self.result = msg
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in ChangeMyPassword method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.result
