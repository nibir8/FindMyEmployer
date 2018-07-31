
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,statusData,Messages4
import sys
import sys, os
from Test_Config import *
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import PostMyStatus
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import PostUserStatus



class Test_PostUserStatus(unittest.TestCase):

  def test_insertUserStatus_1(self):
        status = "My test status"
        postuserstatus = PostUserStatus.PostUserStatus(Emailid[1],status,Messages4[0])
        final_message = postuserstatus.insertUserStatus()
        final_message = 'Successfully posted status'

  def test_insertUserStatus_2(self):
        status = "My test status"
        postuserstatus = PostUserStatus.PostUserStatus(Emailid[2],status,Messages4[0])
        final_message = postuserstatus.insertUserStatus()
        final_message = 'Could not post status'



if __name__ == '__main__':
    unittest.main()
