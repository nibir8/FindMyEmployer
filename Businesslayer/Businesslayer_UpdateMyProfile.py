import os.path
import logging
import sys
from Businesslayer_UpdateMyobject import Businesslayer_UpdateMyobject
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_UpdateMyProfile import Databaselayer_UpdateMyProfile

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_UpdateMyProfile:
    def updateMyProfileMethod_BSL(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list,typeOfUser,typeOfPlan):
        try:
            updateMyobject = Businesslayer_UpdateMyobject()
            updateMyobject.updateMyObjectBSL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,typeOfUser,typeOfPlan,user_details_list)
            databaselayerupdatemyprofile =Databaselayer_UpdateMyProfile()
            msg = databaselayerupdatemyprofile.updateMyProfileMethod_DBL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list)
            return msg
        except Exception as e:
            excep_msg = "Error occured in method updateMyProfileMethod_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
