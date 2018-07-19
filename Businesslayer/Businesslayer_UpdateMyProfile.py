import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_UpdateMyProfile import Databaselayer_UpdateMyProfile

class Businesslayer_UpdateMyProfile:
    def updateMyProfileMethod_BSL(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list):
        try:
            databaselayerupdatemyprofile =Databaselayer_UpdateMyProfile()
            msg = databaselayerupdatemyprofile.updateMyProfileMethod_DBL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list)
            return msg
        except Exception as e:
            msg = "Error occured in method updateMyProfileMethod_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(msg, exc_info=True)
