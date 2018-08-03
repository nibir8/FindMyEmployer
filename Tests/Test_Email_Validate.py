import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid
import sys
from Test_Config import *
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Email_Validate



class Test_Email_Validate(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        formValidate = Email_Validate.Email_Validate()
        result = formValidate.formValidate_BSL(Emailid[0])
        assert result == Emailid[0]

    def test_formValidate_BSL_2(self):
        formValidate = Email_Validate.Email_Validate()
        result = formValidate.formValidate_BSL(Emailid[4])
        assert result == "Email address not valid"

if __name__ == '__main__':
    unittest.main()