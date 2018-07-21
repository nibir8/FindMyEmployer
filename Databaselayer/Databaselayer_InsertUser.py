import hashlib, os
import logging
from extensions import mysql
import IInsertnewUser
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror
sys.path.append(os.path.abspath(os.path.join('0', '../models')))
from User import User


class Databaselayer_InsertUser(IInsertnewUser.IInsertnewUser):
    def insertNewUser_DBL(self,myuser):
        try:
            msg=""
            password = hashlib.md5(myuser.password.encode()).hexdigest()
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spCreateUser',[myuser.password,myuser.email,myuser.firstName,myuser.lastName,myuser.address1,myuser.address2,myuser.zipcode,myuser.city,myuser.state,myuser.country,myuser.phone,myuser.userType,myuser.planType])
            conn.commit()
            msg = "Registered Successfully"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in insertNewUser_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg
