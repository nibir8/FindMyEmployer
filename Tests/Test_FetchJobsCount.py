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
import FetchJobsCount



class Test_FetchJobsCount(unittest.TestCase):
    def test_fetchJobsCount_1(self):
        fetchjobscount = FetchJobsCount.FetchJobsCount(mysql,'rohit.gs28@gmail.com',30,'pass')
        jobsCount,result = fetchjobscount.getJobsCount()
        assert jobsCount == 30
        assert result == 'pass'

    def test_fetchJobsCount_2(self):
        fetchjobscount = FetchJobsCount.FetchJobsCount(mysql,'rohit.gs28@gmail.com',12,'fail')
        jobsCount,result = fetchjobscount.getJobsCount()
        assert jobsCount == 12
        assert result == 'fail'


if __name__ == '__main__':
    unittest.main()
