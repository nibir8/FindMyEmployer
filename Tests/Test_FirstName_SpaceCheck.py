import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Firstname
import sys
from Test_Config import *
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import FirstName_SpaceCheck


class Test_FirstName_SpaceCheck(unittest.TestCase):
    def test_formValidate_BSL_1(self):
        formValidate = FirstName_SpaceCheck.FirstName_SpaceCheck()
        result = formValidate.formValidate_BSL(Firstname[0])
        assert result == Firstname[0]

    def test_formValidate_BSL_2(self):
        formValidate = FirstName_SpaceCheck.FirstName_SpaceCheck()
        result = formValidate.formValidate_BSL("    ")
        assert result == "Firstname not valid"

if __name__ == '__main__':
    unittest.main()