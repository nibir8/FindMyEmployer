
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
import Databaselayer_PostStatus
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_PostStatus



class Businesslayer_PostStatus_Test(unittest.TestCase):

  def test_insertUserStatus_BSL_1(self):
        mockObject = Businesslayer_PostStatus.Businesslayer_PostStatus()
        mockObject.insertUserStatus_BSL = MagicMock(return_value="Successfully posted status")
        mockObject.insertUserStatus_BSL(Emailid[1],'My first status')
        assert mockObject.insertUserStatus_BSL(Emailid[1],'My first status') == "Successfully posted status"

  def test_insertUserStatus_BSL_2(self):
        mockObject = Businesslayer_PostStatus.Businesslayer_PostStatus()
        mockObject.insertUserStatus_BSL = MagicMock(return_value="Could not find user id")
        mockObject.insertUserStatus_BSL(Emailid[2],'My first status')
        assert mockObject.insertUserStatus_BSL(Emailid[2],'My first status') == "Could not find user id"

  def test_insertUserStatus_BSL_3(self):
        mockObject = Businesslayer_PostStatus.Businesslayer_PostStatus()
        mockObject.insertUserStatus_BSL = MagicMock(return_value="Successfully posted status")
        mockObject.insertUserStatus_BSL(Emailid[2],'My first status')
        mockObject.insertUserStatus_BSL.assert_called_with(Emailid[2],'My first status')




if __name__ == '__main__':
    unittest.main()
