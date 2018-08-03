import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,Messages1
import sys
import sys, os

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import CheckIfUserValid
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import CheckIfMyUserValid

class Test_CheckIfMyUserValid(unittest.TestCase):
    def test_isValid_1(self):
        ifUserValid = CheckIfMyUserValid.CheckIfMyUserValid(Emailid[1], Password[1], True,True)
        result = ifUserValid.isValid()
        assert result == True

    def test_isValid_2(self):
        ifUserValid = CheckIfMyUserValid.CheckIfMyUserValid('qwe', Password[1], False,'Invalid UserId / Password')
        result = ifUserValid.isValid()
        assert result == 'Invalid UserId / Password'
		
    def test_isValid_3(self):
        ifUserValid = CheckIfMyUserValid.CheckIfMyUserValid(Emailid[1], 'qwe', False,'Invalid UserId / Password')
        result = ifUserValid.isValid()
        assert result == 'Invalid UserId / Password'
		
    def test_isValid_4(self):
        ifUserValid = CheckIfMyUserValid.CheckIfMyUserValid(Emailid[1], Password[2], False,'Invalid UserId / Password')
        result = ifUserValid.isValid()
        assert result == 'Invalid UserId / Password'

if __name__ == '__main__':
    unittest.main()
