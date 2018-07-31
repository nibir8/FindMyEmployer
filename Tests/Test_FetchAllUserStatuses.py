
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,statusData,Messages3
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import FetchUserStatuses
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import FetchAllUserStatuses



class Test_FetchAllUserStatuses(unittest.TestCase):

  def test_getUserStatus_BSL_1(self):
        statusData = ['My first status', 'felling thoughtful']
        fetchalluserstatuses = FetchAllUserStatuses.FetchAllUserStatuses(statusData,Messages3[0])
        statusData,result = fetchalluserstatuses.getAllUserStatus()
        assert result == 'User Staus Fetched Successfully'

  def test_getUserStatus_BSL_2(self):
        statusData = []
        fetchalluserstatuses = FetchAllUserStatuses.FetchAllUserStatuses(statusData,Messages3[1])
        statusData,result = fetchalluserstatuses.getAllUserStatus()
        assert result == 'Unable to fetch user status'








if __name__ == '__main__':
    unittest.main()
