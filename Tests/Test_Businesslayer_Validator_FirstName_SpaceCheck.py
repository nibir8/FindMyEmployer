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
import Businesslayer_Validator_FirstName_SpaceCheck


class Businesslayer_Validator_FirstName_SpaceCheck_test(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        mockObject = Businesslayer_Validator_FirstName_SpaceCheck.Businesslayer_FirstName_SpaceCheck()
        mockObject.formValidate_BSL = MagicMock(return_value="Firstname not valid")
        mockObject.formValidate_BSL('    ')
        assert mockObject.formValidate_BSL('    ') == "Firstname not valid"

    def test_formValidate_BSL_2(self):
        mockObject = Businesslayer_Validator_FirstName_SpaceCheck.Businesslayer_FirstName_SpaceCheck()
        mockObject.formValidate_BSL = MagicMock(return_value="Nibir")
        mockObject.formValidate_BSL('Nibir')
        assert mockObject.formValidate_BSL('Nibir') == "Nibir"

if __name__ == '__main__':
    unittest.main()