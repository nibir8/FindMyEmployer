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
import Databaselayer_InsertJob
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_InsertJob



class Businesslayer_InsertJobAd_Test(unittest.TestCase):
    def test_insertJobApplication_BSL_1(self):
        mockObject = Businesslayer_InsertJob.Businesslayer_InsertJob()
        mockObject.insertJobApplication_BSL = MagicMock(return_value="Added Job ad")
        mockObject.insertJobApplication_BSL(Emailid[1])
        assert mockObject.insertJobApplication_BSL(Emailid[1]) == "Added Job ad"

    def test_insertJobApplication_BSL_2(self):
        mockObject = Businesslayer_InsertJob.Businesslayer_InsertJob()
        mockObject.insertJobApplication_BSL = MagicMock(return_value="Unable to add job ad")
        mockObject.insertJobApplication_BSL(Emailid[1])
        assert mockObject.insertJobApplication_BSL(Emailid[1]) == "Unable to add job ad"

    def test_insertJobApplication_BSL_3(self):
        mockObject = Businesslayer_InsertJob.Businesslayer_InsertJob()
        mockObject.insertJobApplication_BSL = MagicMock(return_value="Added Job ad")
        mockObject.insertJobApplication_BSL(Emailid[1])
        mockObject.insertJobApplication_BSL.assert_called_with(Emailid[1])

if __name__ == '__main__':
    unittest.main()
