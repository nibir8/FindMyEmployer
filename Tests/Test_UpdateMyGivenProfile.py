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
from extensions import mysql
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..','Databaselayer/')))
from UpdateMyProfile import UpdateMyProfile
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import UpdateMyGivenProfile


class Test_UpdateMyGivenProfile(unittest.TestCase):
    def test_updateMyProfileMethod_1(self):
        updatemyprofile = UpdateMyGivenProfile.UpdateMyGivenProfile("a@a.a","Nibir","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493",User_Details_list,"Employee","plan1","Updated successfully")
        updatemyprofile.updateMyProfileMethod()
        assert updatemyprofile.updateMyProfileMethod() == "Updated successfully"

    def test_updateMyProfileMethod_2(self):
        updatemyprofile = UpdateMyGivenProfile.UpdateMyGivenProfile("a@a.a","Rohit","Gollarahalli","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493",User_Details_list,"Employee","plan1","Unable to update")
        updatemyprofile.updateMyProfileMethod()
        assert updatemyprofile.updateMyProfileMethod() == "Unable to update"


if __name__ == '__main__':
    unittest.main()
