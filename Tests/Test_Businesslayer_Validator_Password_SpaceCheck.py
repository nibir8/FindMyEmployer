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
import Businesslayer_Validator_Password_SpaceCheck


class Businesslayer_Validator_Password_SpaceCheck_test(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        mockObject = Businesslayer_Validator_Password_SpaceCheck.Businesslayer_Password_SpaceCheck()
        mockObject.formValidate_BSL = MagicMock(return_value="Password not valid")
        mockObject.formValidate_BSL('    ')
        assert mockObject.formValidate_BSL('    ') == "Password not valid"

    def test_formValidate_BSL_2(self):
        mockObject = Businesslayer_Validator_Password_SpaceCheck.Businesslayer_Password_SpaceCheck()
        mockObject.formValidate_BSL = MagicMock(return_value=Password[1])
        mockObject.formValidate_BSL(Password[1])
        assert mockObject.formValidate_BSL(Password[1]) == Password[1]

if __name__ == '__main__':
    unittest.main()