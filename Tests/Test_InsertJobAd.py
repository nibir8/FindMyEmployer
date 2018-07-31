import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,Jobdetails,Messages5
import sys
import sys, os
from Test_Config import *
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import InsertMyJob
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import InsertUserJob



class Test_InsertJobAd(unittest.TestCase):
    def test_changeMyProfilePassword_DBL_1(self):
        insertuserjob = InsertUserJob.InsertUserJob(Jobdetails[0],Jobdetails[1],Jobdetails[2],Jobdetails[3],Jobdetails[4],Jobdetails[5],Jobdetails[6],Messages5[0])
        message = insertuserjob.insertUserJob()
        assert message == 'Added Job Successfully'

    def test_changeMyProfilePassword_DBL_2(self):
        insertmyjob = InsertUserJob.InsertUserJob(Jobdetails[0],Jobdetails[1],Jobdetails[2],Jobdetails[3],Jobdetails[4],Jobdetails[5],Emailid[0],Messages5[1])
        message = insertmyjob.insertUserJob()
        assert message == 'Could not add job'


if __name__ == '__main__':
    unittest.main()
