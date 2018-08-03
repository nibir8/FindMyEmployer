import hashlib, os
import logging
import IProfileUpdate
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror



class UpdateMyProfile(IProfileUpdate.IProfileUpdate):
    def __init__(self,mysql,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,result):
        self.mysql = mysql
        self.email = email
        self.firstName =firstName
        self.lastName = lastName
        self.address1 = address1
        self.address2 = address2
        self.zipcode = zipcode
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        self.user_details_list = user_details_list
        self.result = result



    def updateMyProfileMethod(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                logging.info("Creating a new database connection")
                cur.callproc('spUpdateUser',[self.email,self.firstName,self.lastName,self.address1,self.address2,self.city,self.zipcode,self.state,self.country,self.phone,
                self.user_details_list[0],self.user_details_list[1],self.user_details_list[2],self.user_details_list[3],
                self.user_details_list[4],self.user_details_list[5],self.user_details_list[6],
                self.user_details_list[7],self.user_details_list[8],self.user_details_list[9],self.user_details_list[10],
                self.user_details_list[11],self.user_details_list[12],self.user_details_list[13],self.user_details_list[14],
                self.user_details_list[15],self.user_details_list[16],self.user_details_list[17],self.user_details_list[18],
                self.user_details_list[19],self.user_details_list[20],self.user_details_list[21],self.user_details_list[22]])
                conn.commit()
                logging.info("Changes updated in the database")
                self.result  = "pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in updateMyProfileMethod_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            self.result = "fail"
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        logging.info("Closing database connection")
        return self.result
