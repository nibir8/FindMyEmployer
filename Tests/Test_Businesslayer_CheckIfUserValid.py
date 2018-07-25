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
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import Databaselayer_CheckIfUserValid
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_CheckIfUserValid

class Businesslayer_CheckIfUserValid_test(unittest.TestCase):
    def test_isValid_BSL_1(self):
        mockObject = Businesslayer_CheckIfUserValid.Businesslayer_CheckIfUserValid()
        mockObject.isValid_BSL = MagicMock(return_value="Invalid UserId / Password")
        mockObject.isValid_BSL("qwe","qwe")
        assert mockObject.isValid_BSL("qwe","qwe") == "Invalid UserId / Password"

    def test_isValid_BSL_2(self):
        mockObject = Businesslayer_CheckIfUserValid.Businesslayer_CheckIfUserValid()
        mockObject.isValid_BSL = MagicMock(return_value="Invalid UserId / Password")
        mockObject.isValid_BSL(Emailid[1],Password[2])
        assert mockObject.isValid_BSL(Emailid[1],Password[2]) == "Invalid UserId / Password"
		
    def test_isValid_BSL_3(self):
        mockObject = Businesslayer_CheckIfUserValid.Businesslayer_CheckIfUserValid()
        mockObject.isValid_BSL = MagicMock(return_value="Invalid UserId / Password")
        mockObject.isValid_BSL(Emailid[1],"qwe")
        assert mockObject.isValid_BSL(Emailid[1],"qwe") == "Invalid UserId / Password"

    def test_isValid_BSL_4(self):
        mockObject = Businesslayer_CheckIfUserValid.Businesslayer_CheckIfUserValid()
        mockObject.isValid_BSL = MagicMock(return_value="Invalid UserId / Password")
        mockObject.isValid_BSL("qwe",Password[2])
        assert mockObject.isValid_BSL("qwe",Password[2]) == "Invalid UserId / Password"

    def test_isValid_BSL_5(self):
        mockObject = Businesslayer_CheckIfUserValid.Businesslayer_CheckIfUserValid()
        mockObject.isValid_BSL = MagicMock(return_value=True)
        mockObject.isValid_BSL(Emailid[1],Password[1])
        assert mockObject.isValid_BSL(Emailid[1],Password[1]) == True

if __name__ == '__main__':
    unittest.main()
