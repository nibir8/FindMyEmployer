
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,Messages2
import sys
from Test_Config import *
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import InsertMyJobApplication
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import InsertGivenJobApplication


class Test_InsertMyJobApplication(unittest.TestCase):
    def test_insertMyJobApplication_1(self):
        insertmyjobapplication = InsertGivenJobApplication.InsertGivenJobApplication(Emailid[0],Messages2[0])
        result = insertmyjobapplication.insertGivenJobApplication()
        assert result == "pass"

    def test_insertMyJobApplication_2(self):
        insertmyjobapplication = InsertGivenJobApplication.InsertGivenJobApplication(Emailid[0],Messages2[1])
        result = insertmyjobapplication.insertGivenJobApplication()
        assert result == "fail"

if __name__ == '__main__':
    unittest.main()
