import hashlib
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,Messages1,Messages2
import sys
import sys, os

from Test_Config import *

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import CheckIfUserValid


class Test_CheckIfUserValid(unittest.TestCase):
    def test_emailIsValid_1(self):
        email = "rohit@gmail.com"
        listOfUsers = ((u'nibir8@gmail.com', u'202cb962ac59075b964b07152d234b70'), (u'rohit@gmail.com', u'202cb962ac59075b964b07152d234b70'), (u'rohit.gs28@gmail.com', u'202cb962ac59075b964b07152d234b70'), (u'rohit1@gmail.com', u'202cb962ac59075b964b07152d234b70'), (u'rohit.2@gmail.com', u'202cb962ac59075b964b07152d234b70'))
        checkEmailValid = CheckIfUserValid.CheckIfUserValid(mysql,email,"123" ,listOfUsers,'pass')
        result = checkEmailValid.emailIsValid()
        assert result == True
		
if __name__ == '__main__':
    unittest.main()
