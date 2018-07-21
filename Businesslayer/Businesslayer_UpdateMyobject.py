import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_UpdateMyProfile import Databaselayer_UpdateMyProfile

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensionsUser import myUser,myEmployee,myEmployer

class Businesslayer_UpdateMyobject:
    def updateMyObjectBSL(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan):
        try:
            print "Rohit"
            print typeOfUser
            if typeOfUser == "employee":
                myEmployee.firstName = firstName
                myEmployee.lastName = lastName
                myEmployee.address1 = address1
                myEmployee.address2 = address2
                myEmployee.zipcode = zipcode
                myEmployee.city = city
                myEmployee.state = state
                myEmployee.country = country
                myEmployee.phone = phone
                myEmployee.userType = typeOfUser
                myEmployee.plantype = typeOfPlan
                myEmployee.user_details = user_details_list
            elif typeOfUser == "employer":
                myEmployer.firstName = firstName
                myEmployer.lastName = lastName
                myEmployer.address1 = address1
                myEmployer.address2 = address2
                myEmployer.zipcode = zipcode
                myEmployer.city = city
                myEmployer.state = state
                myEmployer.country = country
                myEmployer.phone = phone
                myEmployer.userType = typeOfUser
                myEmployer.plantype = typeOfPlan
                myEmployer.user_details = user_details_list
            #databaselayerupdatemyprofile =Databaselayer_UpdateMyProfile()
            #msg = databaselayerupdatemyprofile.updateMyProfileMethod_DBL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list)
            return msg
        except Exception as e:
            excep_msg = "Error occured in method updateMyProfileMethod_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
