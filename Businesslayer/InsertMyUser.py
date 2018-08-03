import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from InsertUser import InsertUser

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror

class InsertMyUser:
    def __init__(self,email,password,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan,data,result):
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
        self.result = result

    def insertMyNewUser(self):
        try:
            if(self.data == ''):
                insertuser = InsertUser(mysql,self.email,self.password,self.firstName,self.lastName,self.address1,self.address2,self.zipcode,self.city,self.state,self.country,self.phone,self.user_details_list,self.typeOfUser,self.typeOfPlan,self.data)
                self.result = insertuser.insertNewUser()
                return self.result
            return self.result
        except Exception as e:
            excep_msg = "Error occured in method insertNewUser method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
