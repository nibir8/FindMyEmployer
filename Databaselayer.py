import sqlite3, hashlib, os
import logging
import unittest
from extensions import mysql
import main


class IProfileUpdate:
    def updateMyProfileMethod_DBL(Self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list):  raise NotImplementedError
class IPasswordUpdate:
    def changeMyProfilePassword_DBL(Self,email,oldPassword,newPassword): raise NotImplementedError
class ICheckValidity:
    def isValid_DBL(Self,email, password): raise NotImplementedError
class IFetchLoginDetails:
    def getLoginDetails_DBL(self,email): raise NotImplementedError
class IInsertnewUser:
    def insertNewUser_DBL(Self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType): raise NotImplementedError
class IFtechProfileDetails:
    def getProfileData_DBL(Self,email): raise NotImplementedError
class IFetchJobDetails:
    def getJob_DBL(Self,jobId): raise NotImplementedError
class IInsertJobDetails:
    def insertJob_DBL(Self,jobId,companyName,title,manager,location,jobDetails): raise NotImplementedError
class IFetchSearchedProfile:
    def fetchSearchedProfile_DBL(Self,firstName): raise NotImplementedError
class IPostStatus:
    def insertUserStatus(Self,email,status): raise NotImplementedError
    def getUserStatus_DBL(Self): raise NotImplementedError

#Seperated to different classes
class Databaselayer_UpdateMyProfile(IProfileUpdate):
    def updateMyProfileMethod_DBL(Self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list):
        try:
            msg=""
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spUpdateUser',[email,firstName,lastName,address1,address2,city,zipcode,state,country,phone,
            user_details_list[0],user_details_list[1],user_details_list[2],user_details_list[3],
            user_details_list[4],user_details_list[5],user_details_list[6],
            user_details_list[7],user_details_list[8],user_details_list[9],user_details_list[10],
            user_details_list[11],user_details_list[12],user_details_list[13],user_details_list[14],
            user_details_list[15],user_details_list[16],user_details_list[17],user_details_list[18],
            user_details_list[19],user_details_list[20],user_details_list[21],user_details_list[22]])
            conn.commit()
            msg = "Saved Successfully"
        except:
            conn.rollback()
            excep_msg = "Error occured in updateMyProfileMethod_DBL method"
            logging.info(excep_msg, exc_info=True)
            conn.close()
        return msg

class Databaselayer_ChangeMyPassword(IPasswordUpdate):
    def changeMyProfilePassword_DBL(Self,email,oldPassword,newPassword):
        try:
            msg=""
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spFetchUserPassword',[email])
            userId, password = cur.fetchone()
            if (password == oldPassword):
                cur.callproc('spUpdatePassword',[newPassword,userId])
                conn.commit()
                msg="Changed successfully"
            else:
                msg = "Wrong password"
        except:
            conn.rollback()
            excep_msg = "Error occured in changeMyProfilePassword_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg

class Databaselayer_CheckIfUserValid(ICheckValidity):
    def isValid_DBL(Self,email, password):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetAllUsers')
            data = cur.fetchall()
            conn.close()
        except:
            excep_msg = "Error occured in isValid_DBL method"
            logging.info(excep_msg, exc_info=True)
        for row in data:
            if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
                return True
        return False

class Databaselayer_LoginClass(IFetchLoginDetails):
    def getLoginDetails_DBL(self,email):
        try:
            loggedIn = True
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetUserDetails',[email])
            userId, firstName = cur.fetchone()
        except:
            excep_msg = "Error occured in getLoginDetails_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return (loggedIn, firstName)

class Databaselayer_InsertUser(IInsertnewUser):
    def insertNewUser_DBL(Self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType):
        try:
            msg=""
            password = hashlib.md5(password.encode()).hexdigest()
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spCreateUser',[password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType])
            conn.commit()
            msg = "Registered Successfully"
        except:
            conn.rollback()
            excep_msg = "Error occured in insertNewUser_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg

class Databaselayer_FetchUserData(IFtechProfileDetails):
    def getProfileData_DBL(Self,email):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetCompleteUserDetails',[email])
            profileData = cur.fetchone()
        except:
            conn.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return profileData


class Databaselayer_PostStatus(IPostStatus):
    def insertUserStatus_DBL(Self,email,status):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spInsertUserStatus',[email,status])
            conn.commit()
            msg = "Status Added Successfully"
        except:
            conn.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg

class Databaselayer_FetchStatus(IPostStatus):
    def getUserStatus_DBL(Self):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetUserStatus')
            statusData = cur.fetchall()
            #print statusData
            conn.commit()
        except:
            conn.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return statusData

class Databaselayer_InsertJob(IInsertJobDetails):
    def insertJob_DBL(Self,jobId,companyName,title,manager,location,jobDetails):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spInsertJobDetails',[jobId,companyName,title,manager,location,jobDetails])
            conn.commit()
            msg = "Successfully Added"
        except:
            conn.rollback()
            excep_msg = "Error occured in insertJob_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return msg

class Databaselayer_FetchJob(IFetchJobDetails):
    def getJob_DBL(self):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spFetchJobdetails')
            jobData = cur.fetchall()
        except:
            conn.rollback()
            excep_msg = "Error occured in getJob_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return jobData

class Databaselayer_FetchSearchedProfile(IFetchSearchedProfile):
    def fetchSearchedProfile_DBL(self,firstName):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetSearchedUser',[firstName])
            searchedProfileData = cur.fetchall()
        except:
            conn.rollback()
            excep_msg = "Error occured in fetchSearchedProfile_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return searchedProfileData
