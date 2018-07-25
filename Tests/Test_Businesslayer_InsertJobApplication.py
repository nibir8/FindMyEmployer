
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import Databaselayer_InsertJobApplication
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_InsertJobApplication


class Businesslayer_InsertJobApplication_Test(unittest.TestCase):
    def test_insertJobApplication_BSL_1(self):
        mockObject = Businesslayer_InsertJobApplication.Businesslayer_InsertJobApplication()
        mockObject.insertJobApplication_BSL = MagicMock(return_value="Added Job application")
        mockObject.insertJobApplication_BSL(Emailid[1])
        assert mockObject.insertJobApplication_BSL(Emailid[1]) == "Added Job application"

    def test_insertJobApplication_BSL_2(self):
        mockObject = Businesslayer_InsertJobApplication.Businesslayer_InsertJobApplication()
        mockObject.insertJobApplication_BSL = MagicMock(return_value="Unable to add job applicatoin")
        mockObject.insertJobApplication_BSL(Emailid[1])
        assert mockObject.insertJobApplication_BSL(Emailid[1]) == "Unable to add job applicatoin"

    def test_insertJobApplication_BSL_3(self):
        mockObject = Businesslayer_InsertJobApplication.Businesslayer_InsertJobApplication()
        mockObject.insertJobApplication_BSL = MagicMock(return_value="Added Job application")
        mockObject.insertJobApplication_BSL(Emailid[1])
        mockObject.insertJobApplication_BSL.assert_called_with(Emailid[1])

if __name__ == '__main__':
    unittest.main()
