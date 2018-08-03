import os.path
import logging
import sys

from UpdateMyUserobject import UpdateMyUserobject

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from UpdateMyProfile import UpdateMyProfile

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensions import mysql


class UpdateMyGivenProfile:
    def __init__(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan,msg):
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
        self.typeOfUser = typeOfUser
        self.typeOfPlan = typeOfPlan
        self.finalMessage = msg


    def set_messages(self,argument):
        return{
            'pass': 'Updated successfully',
            'fail': 'Unable to update'
        }.get(argument, 'Invalid password')



    def updateMyProfileMethod(self):
        try:
            updateMyobject = UpdateMyUserobject(self.email,self.firstName,self.lastName,self.address1,self.address2,self.zipcode,self.city,self.state,self.country,self.phone,self.typeOfUser,self.typeOfPlan,self.user_details_list)
            updateMyobject.updateMyObject()
            if self.finalMessage == "":
                updatemyprofile =UpdateMyProfile(mysql,self.email,self.firstName,self.lastName,self.address1,self.address2,self.zipcode,self.city,self.state,self.country,self.phone,self.user_details_list,'')
                status = updatemyprofile.updateMyProfileMethod()
                self.finalMessage = self.set_messages(status)
            return self.finalMessage
        except Exception as e:
            excep_msg = "Error occured in method updateMyProfileMethod method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
