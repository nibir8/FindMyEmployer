import sqlite3, hashlib, os
import logging
import unittest


class IProfileInterface:
    def updateMyProfileMethod_DBL(Self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):  raise NotImplementedError
    def changeMyProfilePassword_DBL(Self,myemail,oldPassword,newPassword): raise NotImplementedError
    def isValid_DBL(Self,email, password): raise NotImplementedError
    def getLoginDetails_DBL(self,myemail): raise NotImplementedError
    def insertNewUser_DBL(Self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone): raise NotImplementedError
    def getProfileData_DBL(Self,myemail): raise NotImplementedError



#Seperated to different classes
class Databaselayer_UpdateMyProfile(IProfileInterface):
    def updateMyProfileMethod_DBL(Self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
            with sqlite3.connect('database.db') as con:
                    try:
                        cur = con.cursor()
                        cur.execute('UPDATE users SET firstName = ?, lastName = ?, address1 = ?, address2 = ?, zipcode = ?, city = ?, state = ?, country = ?, phone = ? WHERE email = ?', (firstName, lastName, address1, address2, zipcode, city, state, country, phone, email))

                        con.commit()
                        msg = "Saved Successfully"
                    except:
                        con.rollback()
                        excep_msg = "Error occured in updateMyProfileMethod_DBL method"
                        logging.info(excep_msg, exc_info=True)
            con.close()
            return msg


class Databaselayer_ChangeMyPassword(IProfileInterface):
    def changeMyProfilePassword_DBL(Self,myemail,oldPassword,newPassword):
        try:
            msg=""
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("SELECT userId, password FROM users WHERE email = '" + myemail + "'")
                userId, password = cur.fetchone()
                print password
                if (password == oldPassword):
                        cur.execute("UPDATE users SET password = ? WHERE userId = ?", (newPassword, userId))
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

class Databaselayer_CheckIfUserValid(IProfileInterface):
    def isValid_DBL(Self,email, password):
        try:
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT email, password FROM users')
            data = cur.fetchall()
            con.close()
        except:
            excep_msg = "Error occured in isValid_DBL method"
            logging.info(excep_msg, exc_info=True)
        for row in data:
            if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
                return True
        return False

class Databaselayer_LoginClass(IProfileInterface):
    def getLoginDetails_DBL(self,myemail):
        try:
            loggedIn = True
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("SELECT userId, firstName FROM users WHERE email = '" + myemail + "'")
                userId, firstName = cur.fetchone()
        except:
            excep_msg = "Error occured in getLoginDetails_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return (loggedIn, firstName)

class Databaselayer_InsertUser(IProfileInterface):
    def insertNewUser_DBL(Self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
        try:
            with sqlite3.connect('database.db') as con:

                    cur = con.cursor()
                    cur.execute('INSERT INTO users (password, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (hashlib.md5(password.encode()).hexdigest(), email, firstName, lastName, address1, address2, zipcode, city, state, country, phone))
                    con.commit()
                    msg = "Registered Successfully"
        except:
                con.rollback()
                excep_msg = "Error occured in insertNewUser_DBL method"
                logging.info(excep_msg, exc_info=True)
        con.close()
        return msg


class Databaselayer_FetchUserData(IProfileInterface):
    def getProfileData_DBL(Self,myemail):
        try:
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("SELECT userId, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone FROM users WHERE email = '" + myemail + "'")
                profileData = cur.fetchone()
        except:
            con.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return profileData
