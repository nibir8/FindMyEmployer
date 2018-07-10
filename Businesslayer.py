import Databaselayer
from Databaselayer import *


class Businesslayer_LoginClass:
    def getLoginDetails_BSL(self,myemail):
        try:
            getlogindetails = Databaselayer_LoginClass()
            loggedIn, firstName = getlogindetails.getLoginDetails_DBL(myemail)
            return (loggedIn, firstName)
        except:
            msg = "Error occured in method getLoginDetails_BSL method"
            logging.info(msg, exc_info=True)

class Businesslayer_UpdateMyProfile:
    def updateMyProfileMethod_BSL(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
        try:
            databaselayerupdatemyprofile = Databaselayer_UpdateMyProfile()
            msg = databaselayerupdatemyprofile.updateMyProfileMethod_DBL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
            return msg
        except:
            msg = "Error occured in method updateMyProfileMethod_BSL method"
            logging.info(msg, exc_info=True)


class Businesslayer_ChangeMyPassword:
    def changeMyProfilePassword_BSL(Self,myemail,oldPassword,newPassword):
        try:
            changemypassword = Databaselayer_ChangeMyPassword()
            msg = changemypassword.changeMyProfilePassword_DBL(myemail,oldPassword,newPassword)
            return msg
        except:
            msg = "Error occured in method changeMyProfilePassword_BSL method"
            logging.info(msg, exc_info=True)

class Businesslayer_FetchUserData:
    def getProfileData_BSL(Self,myemail):
        try:
            fetchuserdata = Databaselayer_FetchUserData()
            profileData = fetchuserdata.getProfileData_DBL(myemail)
            return profileData
        except:
            msg = "Error occured in method getProfileData_BSL method"
            logging.info(msg, exc_info=True)


class Businesslayer_CheckIfUserValid:
    def isValid_BSL(self,email, password):
        try:
            checkifuseremailisvalid = Databaselayer_CheckIfUserValid()
            value = checkifuseremailisvalid.isValid_DBL(email, password)
            return value
        except:
            msg = "Error occured in method isValid_BSL method"
            logging.info(msg, exc_info=True)

class Businesslayer_InsertUser:
    def insertNewUser_BSL(self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
        try:
            insertuser = Databaselayer_InsertUser()
            insertuser.insertNewUser_DBL(password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
        except:
            msg = "Error occured in method insertNewUser_BSL method"
            logging.info(msg, exc_info=True)
