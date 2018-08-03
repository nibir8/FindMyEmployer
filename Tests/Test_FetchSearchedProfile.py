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
from Test_Config import *
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..','Databaselayer/')))
import FetchSearchedProfile
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import FetchMySearchedProfile



class Test_FetchSearchedProfile(unittest.TestCase):
    def test_fetchMySearchedProfile_1(self):
        fetchSearchedProfile = ["a@a.a","Nibir","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada","9008491493"]
        fetchsearchedProfile = FetchSearchedProfile.FetchSearchedProfile(mysql,"Nibir",fetchSearchedProfile,"pass")
        fetchSearchedProfileData,status = fetchsearchedProfile.fetchSearchedProfile()
        assert status== "pass"

    def test_fetchMySearchedProfile_2(self):
        fetchSearchedProfile = []
        fetchsearchedProfile = FetchSearchedProfile.FetchSearchedProfile(mysql,"Nibir",fetchSearchedProfile,"fail")
        fetchSearchedProfileData,status = fetchsearchedProfile.fetchSearchedProfile()
        assert status== "fail"

if __name__ == '__main__':
    unittest.main()
