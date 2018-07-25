
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,statusData
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import Databaselayer_FetchStatus
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_GetStatus



class Businesslayer_GetStatus_Test(unittest.TestCase):

  def test_getUserStatus_BSL_1(self):
        statusData = ['My first status', 'felling thoughtful']
        mockObject = Businesslayer_GetStatus.Businesslayer_GetStatus()
        mockObject.getUserStatus_BSL = MagicMock(return_value=statusData)
        mockObject.getUserStatus_BSL()
        assert mockObject.getUserStatus_BSL() == statusData







if __name__ == '__main__':
    unittest.main()
