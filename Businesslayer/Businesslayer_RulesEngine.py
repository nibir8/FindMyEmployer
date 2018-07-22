import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_UpdateMyProfile import Databaselayer_UpdateMyProfile

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

sys.path.append(os.path.abspath(os.path.join('0', '../DecoraterClasses')))
from Employee import Employee
from Employee_Plan1_decorator import Employee_Plan1_decorator

class Businesslayer_RulesEngine:
    def rulesEngine_BSL(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan):
        try:
            print "Rohit"
            print typeOfUser
            if typeOfUser == "employee":
                myEmployee = Employee(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan)


            elif typeOfUser == "employer":
                myEmployer = Employer(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan)

            return msg
        except Exception as e:
            excep_msg = "Error occured in method updateMyProfileMethod_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
