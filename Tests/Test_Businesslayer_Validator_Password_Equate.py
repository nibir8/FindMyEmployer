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
import Businesslayer_Validator_Password_Equate


class Businesslayer_Validator_Password_Equate_test(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        mockObject = Businesslayer_Validator_Password_Equate.Businesslayer_Password_Equate()
        mockObject.formValidate_BSL = MagicMock(return_value="123")
        mockObject.formValidate_BSL('123','123')
        assert mockObject.formValidate_BSL('123','123') == "123"

    def test_formValidate_BSL_2(self):
        mockObject = Businesslayer_Validator_Password_Equate.Businesslayer_Password_Equate()
        mockObject.formValidate_BSL = MagicMock(return_value="Two Passwords do not match")
        mockObject.formValidate_BSL('123','1234')
        assert mockObject.formValidate_BSL('123','1234') == "Two Passwords do not match"

if __name__ == '__main__':
    unittest.main()