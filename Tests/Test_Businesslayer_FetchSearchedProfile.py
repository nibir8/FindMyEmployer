import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import User_Details_list
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..','Models/')))
import MyUser

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..','Databaselayer/')))
from Databaselayer_FetchSearchedProfile import Databaselayer_FetchSearchedProfile
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_FetchSearchedProfile



class Businesslayer_FetchSearchedProfile_Test(unittest.TestCase):
    def test_fetchSearchedProfile_BSL_1(self):
        fetchSearchedProfile = ["a@a.a","123","Nibir","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493"]
        mockObject = Businesslayer_FetchSearchedProfile.Businesslayer_FetchSearchedProfile()
        mockObject.fetchSearchedProfile_BSL = MagicMock(return_value=(fetchSearchedProfile,"Successfully Fetched user data"))
        mockObject.fetchSearchedProfile_BSL("Nibir")
        assert mockObject.fetchSearchedProfile_BSL("Nibir") == (fetchSearchedProfile,"Successfully Fetched user data")

    def test_fetchSearchedProfile_BSL_2(self):
        fetchSearchedProfile = []
        mockObject = Businesslayer_FetchSearchedProfile.Businesslayer_FetchSearchedProfile()
        mockObject.fetchSearchedProfile_BSL = MagicMock(return_value=(fetchSearchedProfile,"Unable to fetch user data"))
        mockObject.fetchSearchedProfile_BSL("Rohit")
        assert mockObject.fetchSearchedProfile_BSL("Rohit") == (fetchSearchedProfile,"Unable to fetch user data")

if __name__ == '__main__':
    unittest.main()
