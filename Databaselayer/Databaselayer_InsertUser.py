import hashlib, os
import logging
from extensions import mysql
import IInsertnewUser
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql


class Databaselayer_InsertUser(IInsertnewUser.IInsertnewUser):
    def insertNewUser_DBL(Self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType):
        try:
            msg=""
            password = hashlib.md5(password.encode()).hexdigest()
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spCreateUser',[password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType])
            conn.commit()
            msg = "Registered Successfully"
        except:
            conn.rollback()
            excep_msg = "Error occured in insertNewUser_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg
