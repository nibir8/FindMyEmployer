
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,statusData,Messages2
import sys
import sys, os
from Test_Config import *
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import PostMyStatus


class Test_PostMyStatus(unittest.TestCase):

  def test_insertUserStatus_1(self):
        status = "My test status"
        postuserstatus = PostMyStatus.PostMyStatus(mysql,Emailid[1],status,Messages2[0])
        final_message = postuserstatus.insertMyUserStatus()
        final_message = 'pass'

  def test_insertUserStatus_2(self):
        status = "My test status"
        postuserstatus = PostMyStatus.PostMyStatus(mysql,Emailid[2],status,Messages2[0])
        final_message = postuserstatus.insertMyUserStatus()
        final_message = 'fail'



if __name__ == '__main__':
    unittest.main()
