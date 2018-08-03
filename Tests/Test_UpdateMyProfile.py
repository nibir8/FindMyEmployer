import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import User_Details_list
import sys
import sys, os

from Test_Config import *
sys.path.append(os.path.abspath(os.path.join('..','Models/')))
import MyUser
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..','Databaselayer/')))
import UpdateMyProfile


class Test_UpdateMyProfile(unittest.TestCase):
    def test_updateMyProfileMethod_1(self):
        updatemygivenprofile = UpdateMyProfile.UpdateMyProfile(mysql,"a@a.a","Nibir","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493",User_Details_list,"pass")
        updatemygivenprofile.updateMyProfileMethod()
        assert updatemygivenprofile.updateMyProfileMethod() == "pass"

    def test_updateMyProfileMethod_2(self):
        updatemygivenprofile = UpdateMyProfile.UpdateMyProfile(mysql,"a@a.a","Rohit","Gollarahalli","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493",User_Details_list,"fail")
        updatemygivenprofile.updateMyProfileMethod()
        assert updatemygivenprofile.updateMyProfileMethod() == "fail"


if __name__ == '__main__':
    unittest.main()
