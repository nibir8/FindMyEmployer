
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from Test_Config import *
from MockData import Emailid,Password,statusData,Messages2
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import FetchUserStatuses



class Test_FetchUserStatuses(unittest.TestCase):

  def test_getUserStatuses_1(self):
        statusData = ['My first status', 'felling thoughtful']
        fetchuserstatuses = FetchUserStatuses.FetchUserStatuses(mysql,statusData,Messages2[0])
        statusData,result = fetchuserstatuses.getUserStatuses()
        #assert result == "pass"

  def test_getUserStatuses_2(self):
        statusData = []
        fetchuserstatuses = FetchUserStatuses.FetchUserStatuses(mysql,statusData,Messages2[1])
        statusData,result = fetchuserstatuses.getUserStatuses()
        #assert result == "fail"








if __name__ == '__main__':
    unittest.main()
