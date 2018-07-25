
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password
import sys
import sys, os

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import Databaselayer_ChangeMyPassword
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_ChangeMyPassword


class Businesslayer_ChangeMyPassword_Test(unittest.TestCase):
    def test_changeMyProfilePassword_BSL_1(self):
        mockObject = Businesslayer_ChangeMyPassword.Businesslayer_ChangeMyPassword()
        mockObject.changeMyProfilePassword_BSL = MagicMock(return_value="Changed successfully")
        mockObject.changeMyProfilePassword_BSL(Emailid[1], Password[1], Password[2])
        assert mockObject.changeMyProfilePassword_BSL(Emailid[1], Password[1], Password[2]) == "Changed successfully"

    def test_changeMyProfilePassword_BSL_2(self):
        mockObject = Businesslayer_ChangeMyPassword.Businesslayer_ChangeMyPassword()
        mockObject.changeMyProfilePassword_BSL = MagicMock(return_value="Invalid user password")
        mockObject.changeMyProfilePassword_BSL(Emailid[2], Password[2], Password[1])
        assert mockObject.changeMyProfilePassword_BSL(Emailid[2], Password[2], Password[1]) == "Invalid user password"

    def test_changeMyProfilePassword_BSL_3(self):
        mockObject = Businesslayer_ChangeMyPassword.Businesslayer_ChangeMyPassword()
        mockObject.changeMyProfilePassword_BSL = MagicMock(return_value="The below password is same as previous password")
        mockObject.changeMyProfilePassword_BSL(Emailid[2], Password[2], Password[2])
        assert mockObject.changeMyProfilePassword_BSL(Emailid[2], Password[2], Password[2]) == 'The below password is same as previous password'

    def test_changeMyProfilePassword_BSL_4(self):
        mockObject = Businesslayer_ChangeMyPassword.Businesslayer_ChangeMyPassword()
        mockObject.changeMyProfilePassword_BSL = MagicMock(return_value="Changed successfully")
        mockObject.changeMyProfilePassword_BSL(Emailid[1], Password[1], Password[2])
        mockObject.changeMyProfilePassword_BSL.assert_called_with(Emailid[1], Password[1], Password[2])

if __name__ == '__main__':
    unittest.main()
