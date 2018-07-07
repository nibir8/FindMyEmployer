import Databaselayer
from Databaselayer import *


class Businesslayer_LoginClass:
    def getLoginDetails_BSL(self,myemail):
        getlogindetails = Databaselayer_LoginClass()
        loggedIn, firstName = getlogindetails.getLoginDetails_DBL(myemail)
        return (loggedIn, firstName)


class Businesslayer_UpdateMyProfile:
    def updateMyProfileMethod_BSL(self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
        databaselayerupdatemyprofile = Databaselayer_UpdateMyProfile()
        msg = databaselayerupdatemyprofile.updateMyProfileMethod_DBL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
        return msg


class Businesslayer_ChangeMyPassword:
    def changeMyProfilePassword_BSL(Self,myemail,oldPassword,newPassword):
        changemypassword = Databaselayer_ChangeMyPassword()
        msg = changemypassword.Databaselayer_changeMyProfilePassword(myemail,oldPassword,newPassword)
        return msg

class Businesslayer_FetchUserData:
    def getProfileData_BSL(Self,myemail):
        fetchuserdata = Databaselayer_FetchUserData()
        profileData = fetchuserdata.getProfileData_DBL(myemail)
        return profileData


class Businesslayer_CheckIfUserValid:
    def isValid_BSL(self,email, password):
        checkifuseremailisvalid = Databaselayer_CheckIfUserValid()
        value = checkifuseremailisvalid.isValid_DBL(email, password)
        return value

class Businesslayer_InsertUser:
    def insertNewUser_BSL(self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
        insertuser = Databaselayer_InsertUser()
        insertuser.insertNewUser_DBL(password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
