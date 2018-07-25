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
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_Validator_Email_Validate


class Businesslayer_Validator_Email_Validate_test(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        mockObject = Businesslayer_Validator_Email_Validate.Businesslayer_Email_Validate()
        mockObject.formValidate_BSL = MagicMock(return_value="nibir.mukherjee18@gmail.com")
        mockObject.formValidate_BSL('nibir.mukherjee18@gmail.com')
        assert mockObject.formValidate_BSL('nibir.mukherjee18@gmail.com') == "nibir.mukherjee18@gmail.com"

    def test_formValidate_BSL_2(self):
        mockObject = Businesslayer_Validator_Email_Validate.Businesslayer_Email_Validate()
        mockObject.formValidate_BSL = MagicMock(return_value="Email address not valid")
        mockObject.formValidate_BSL('a  a@a . a')
        assert mockObject.formValidate_BSL('a  a@a . a') == "Email address not valid"

if __name__ == '__main__':
    unittest.main()