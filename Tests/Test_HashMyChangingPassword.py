
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,Messages1
import sys
import sys, os

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import ChangeMyPassword
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import HashMyChangingPassword


class Test_HashMyChangingPassword(unittest.TestCase):
    def test_hashMyChangingPassword_1(self):
        hashMyChangingPassword = HashMyChangingPassword.HashMyChangingPassword(Emailid[1], Password[1], Password[2],Messages1[0])
        result = hashMyChangingPassword.hashMyChangingPassword()
        assert result == "Changed Successfully"

    def test_hashMyChangingPassword_2(self):
        hashMyChangingPassword = HashMyChangingPassword.HashMyChangingPassword(Emailid[1], Password[2], Password[2],Messages1[1])
        result = hashMyChangingPassword.hashMyChangingPassword()
        assert result == "Wrong password"

if __name__ == '__main__':
    unittest.main()
