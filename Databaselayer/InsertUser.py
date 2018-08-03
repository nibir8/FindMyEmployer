import hashlib, os
import logging
from extensions import mysql
import IInsertnewUser
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class InsertUser(IInsertnewUser.IInsertnewUser):
    def __init__(self,mysql,email,password,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan,data):
        self.mysql = mysql
        self.email =email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.address1 = address1
        self.address2 = address2
        self.zipcode = zipcode
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        self.user_details_list = user_details_list
        self.typeOfUser = typeOfUser
        self.typeOfPlan = typeOfPlan
        self.data = data

    def insertNewUser(self):
        try:
            self.data=""
            self.password = hashlib.md5(self.password.encode()).hexdigest()
            conn = self.mysql.connect()
            cur = conn.cursor()
            if (self.data == ''):
                cur.callproc('spCreateUser',[self.password,self.email,self.firstName,self.lastName,self.address1,self.address2,self.zipcode,self.city,self.state,self.country,self.phone,self.typeOfUser,self.typeOfPlan])
                conn.commit()
                self.data = "Registered Successfully"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in insertNewUser method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.data
