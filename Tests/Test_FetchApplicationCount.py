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
import FetchGetApplicationCount



class Test_FetchApplicationCount(unittest.TestCase):
    def test_FetchApplicationCount_1(self):
        fetchapplicationcount = FetchGetApplicationCount.FetchGetApplicationCount(mysql,'rohit.gs28@gmail.com',30,'pass')
        applicationCount,result = fetchapplicationcount.getApplicationCount()
        assert applicationCount == 30
        assert result == 'pass'

    def test_FetchApplicationCount_2(self):
        fetchapplicationcount = FetchGetApplicationCount.FetchGetApplicationCount(mysql,'rohit.gs28@gmail.com',12,'fail')
        applicationCount,result = fetchapplicationcount.getApplicationCount()
        assert applicationCount == 12
        assert result == 'fail'


if __name__ == '__main__':
    unittest.main()
