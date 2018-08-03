import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import User_Details_list
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..','Models/')))
import MyUser

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
from extensionsUser import myUser
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import UpdateMyUserobject




class Test_UpdateMyobject(unittest.TestCase):
    def test_updateMyObject_1(self):
        myUser.email = "a@a.a"
        myUser.firstName = "Nibir"
        myUser.lastName = "Mukherjee"
        myUser.address1 = "1333"
        myUser.address2 = "South"
        myUser.zipcode = "B3J 2K9"
        myUser.city = "Halifax"
        myUser.state = "NS"
        myUser.country = "Canada"
        myUser.phone = "9008491493"
        myUser.userType = "Employee"
        myUser.planType = "plan1"
        myUser.user_details = User_Details_list
        updateMyObject = UpdateMyUserobject.UpdateMyUserobject("a@a.a","Nibir","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493",User_Details_list,"Employee","plan1")
        myobject = updateMyObject.updateMyObject()
        assert myobject == myUser

    def test_updateMyObject_1(self):
        myUser.email = "rohit.gs28@gmail.com"
        myUser.firstName = "Rohit"
        myUser.lastName = "Gollarahallo"
        myUser.address1 = "1333"
        myUser.address2 = "South"
        myUser.zipcode = "B3J 2K9"
        myUser.city = "Halifax"
        myUser.state = "NS"
        myUser.country = "Canada"
        myUser.phone = "9008491493"
        myUser.userType = "Employer"
        myUser.planType = "plan2"
        myUser.user_details = User_Details_list
        updateMyObject = UpdateMyUserobject.UpdateMyUserobject("rohit.gs28@gmail.com","Rohit","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493",User_Details_list,"Employer","plan2")
        myobject = updateMyObject.updateMyObject()
        assert myobject == myUser


if __name__ == '__main__':
    unittest.main()
