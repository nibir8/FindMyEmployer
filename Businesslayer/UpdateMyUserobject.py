import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensionsUser import myUser

class UpdateMyUserobject:
    def __init__(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan):
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

    def updateMyObject(self):
        try:
            myUser.email = self.email
            myUser.firstName = self.firstName
            myUser.lastName = self.lastName
            myUser.address1 = self.address1
            myUser.address2 = self.address2
            myUser.zipcode = self.zipcode
            myUser.city = self.city
            myUser.state = self.state
            myUser.country = self.country
            myUser.phone = self.phone
            myUser.userType = self.typeOfUser
            myUser.planType = self.typeOfPlan
            myUser.user_details = self.user_details_list
            return myUser
        except Exception as e:
            excep_msg = "Error occured in method updateMyProfileMethod_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
