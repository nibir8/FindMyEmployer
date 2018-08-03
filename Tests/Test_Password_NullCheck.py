import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Password
import sys
from Test_Config import *
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Password_NullCheck


class Test_Password_NullCheck(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        formValidate = Password_NullCheck.Password_NullCheck()
        result = formValidate.formValidate_BSL("")
        assert result == "Dont leave userId/Password blank"

if __name__ == '__main__':
    unittest.main()