import os
import hashlib
from .. import database
import unittest
import sqlite3
from .. import Databaselayer
from Databaselayer import *

class Databaselayer_Tests(unittest.TestCase):

'''
    def test_updateMyProfileMethod_DBL(self):
        obj1 = Databaselayer.Databaselayer_UpdateMyProfile()
        password = "Hello!@#"
        email = "rohit.gs28@gmail.com"
        firstName = "Rohit"
        lastName = "Gollarahalli"
        address1 = "#21,Gopika nest"
        address2 = "Bangalore"
        zipcode = "560061"
        city = "Bangalore"
        state = "Karnataka"
        country = "India"
        phone = "9008491493"
        msg = database.Databaselayer.Databaselayer_UpdateMyProfile.updateMyProfileMethod_DBL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
        print msg
        self.assertEqual(msg,"Saved Successfully")


    def test_changeMyProfilePassword_DBL(self):
        obj2 = Databaselayer.Databaselayer_ChangeMyPassword()
        myemail = "rohit.gs28@gmail.com"
        oldPassword = "123"
        newPassword ="1234"
        oldPassword = hashlib.md5(oldPassword.encode()).hexdigest()
        newPassword = hashlib.md5(newPassword.encode()).hexdigest()
        self.assertEqual(obj2.changeMyProfilePassword_DBL(myemail,oldPassword,newPassword),"Changed successfully")

    def test_isValid_DBL_1(self):
        obj3 =  Databaselayer.Databaselayer_CheckIfUserValid()
        email = "rohit.gs28@gmail.com"
        password = "123"
        self.assertEqual(obj3.isValid_DBL(email,password),True)

    def test_isValid_DBL_2(self):
        obj4 = Databaselayer.Databaselayer_CheckIfUserValid()
        email = "rohit.gs28@gmail.com"
        password = "12345"
        self.assertEqual(obj4.isValid_DBL(email,password),False)

    def test_getLoginDetails_DBL(self):
        obj5 = Databaselayer.Databaselayer_LoginClass()
        email = "rohit.gs28@gmail.com"
        self.assertEqual(obj5.getLoginDetails_DBL(email),("rohit.gs28@gmail.com","Rohit"))



'''

if __name__ == '__main__':
    unittest.main()
