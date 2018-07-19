import hashlib, os
import logging
import IPasswordUpdate
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql


class Databaselayer_ChangeMyPassword(IPasswordUpdate.IPasswordUpdate):
    def changeMyProfilePassword_DBL(Self,email,oldPassword,newPassword):
        try:
            msg=""
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spFetchUserPassword',[email])
            userId, password = cur.fetchone()
            if (password == oldPassword):
                cur.callproc('spUpdatePassword',[newPassword,userId])
                conn.commit()
                msg="Changed successfully"
            else:
                msg = "Wrong password"
        except:
            conn.rollback()
            excep_msg = "Error occured in changeMyProfilePassword_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg
