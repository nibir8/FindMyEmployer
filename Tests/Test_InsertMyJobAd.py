import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,Jobdetails,Messages5,Messages2
import sys
import sys, os
from Test_Config import *
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import InsertMyJob



class Test_InsertMyJobAd(unittest.TestCase):
    def test_changeMyProfilePassword_DBL_1(self):
        insertmyjob = InsertMyJob.InsertMyJob(mysql,Jobdetails[0],Jobdetails[1],Jobdetails[2],Jobdetails[3],Jobdetails[4],Jobdetails[5],Jobdetails[6],Messages2[0])
        result = insertmyjob.insertMyJob()
        assert result == 'pass'

    def test_changeMyProfilePassword_DBL_2(self):
        insertmyjob = InsertMyJob.InsertMyJob(mysql,Jobdetails[0],Jobdetails[1],Jobdetails[2],Jobdetails[3],Jobdetails[4],Jobdetails[5],Emailid[0],Messages2[1])
        result = insertmyjob.insertMyJob()
        assert result == 'fail'


if __name__ == '__main__':
    unittest.main()
