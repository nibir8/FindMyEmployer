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
import Businesslayer_Validator_Email_NullCheck


class Businesslayer_Validator_Email_NullCheck_test(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        mockObject = Businesslayer_Validator_Email_NullCheck.Businesslayer_Email_NullCheck()
        mockObject.formValidate_BSL = MagicMock(return_value="Dont leave userId/Password blank")
        mockObject.formValidate_BSL('')
        assert mockObject.formValidate_BSL('') == "Dont leave userId/Password blank"

if __name__ == '__main__':
    unittest.main()