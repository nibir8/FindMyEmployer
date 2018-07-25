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
import Databaselayer_LoginClass
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_LoginClass


class Businesslayer_LoginClass_test(unittest.TestCase):
    def test_getLoginDetails_BSL_1(self):
        mockObject = Businesslayer_LoginClass.Businesslayer_LoginClass()
        mockObject.getLoginDetails_BSL = MagicMock(return_value=(True,Firstname[1],TypeOfUser[1]))
        mockObject.getLoginDetails_BSL(Emailid[1])
        assert mockObject.getLoginDetails_BSL(Emailid[1]) == (True,"Nibir","Employee")

    def test_getLoginDetails_BSL_2(self):
        mockObject = Businesslayer_LoginClass.Businesslayer_LoginClass()
        mockObject.getLoginDetails_BSL = MagicMock(return_value="Invalid UserId/Password")
        mockObject.getLoginDetails_BSL(Emailid[1])
        assert mockObject.getLoginDetails_BSL(Emailid[1]) == "Invalid UserId/Password"

if __name__ == '__main__':
    unittest.main()