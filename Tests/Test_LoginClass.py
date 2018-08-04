import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import *
import sys
import sys, os

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import LoginClass
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import LoginMyClass


class Test_LoginMyClass(unittest.TestCase):
    def test_getLoginDetails_1(self):
        mockObject = LoginMyClass.LoginMyClass(Emailid[1],True, Firstname[1], TypeOfUser[1],'','pass')
        mockObject.getLoginDetails = MagicMock(return_value=(True,Firstname[1],TypeOfUser[1]))
        loggedIn, FirstName, TypeOFUser = mockObject.getLoginDetails()
        assert (loggedIn) == (True)

    def test_getLoginDetails_2(self):
        mockObject = LoginMyClass.LoginMyClass(Emailid[1],False, Firstname[1], TypeOfUser[1],'','pass')
        mockObject.getLoginDetails = MagicMock(return_value=(False,Firstname[1],TypeOfUser[1]))
        loggedIn1, FirstName1, TypeOFUser1 = mockObject.getLoginDetails()
        assert loggedIn1 == False

if __name__ == '__main__':
    unittest.main()