
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
import ChangeMyPassword


class Test_ChangeMyPassword(unittest.TestCase):
    def test_changeMyProfilePassword_DBL_1(self):
        changemypassword = ChangeMyPassword.ChangeMyPassword(Emailid[1], Password[1], Password[2], mysql, Messages2[0])
        result = changemypassword.changeMyProfilePassword()
        assert result == "pass"

    def test_changeMyProfilePassword_DBL_2(self):
        changemypassword = ChangeMyPassword.ChangeMyPassword(Emailid[1], Password[2], Password[2],mysql, Messages2[1])
        result = changemypassword.changeMyProfilePassword()
        assert result == "fail"

if __name__ == '__main__':
    unittest.main()
