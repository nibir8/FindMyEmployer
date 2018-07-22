import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensionsUser import myUser

class Businesslayer_UpdateMyobject:
    def updateMyObjectBSL(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan):
        try:
            myUser.email = email
            myUser.firstName = firstName
            myUser.lastName = lastName
            myUser.address1 = address1
            myUser.address2 = address2
            myUser.zipcode = zipcode
            myUser.city = city
            myUser.state = state
            myUser.country = country
            myUser.phone = phone
            myUser.userType = typeOfUser
            myUser.planType = typeOfPlan
            myUser.user_details = user_details_list
        except Exception as e:
            excep_msg = "Error occured in method updateMyProfileMethod_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
