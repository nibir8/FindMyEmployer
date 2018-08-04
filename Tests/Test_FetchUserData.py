
import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import Emailid,Password,Profiledata
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..','Models/')))
import MyUser
sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
import extensionsUser
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Databaselayer/')))
import FetchUserData
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import FetchMyUserData


class Test_FetchMyUserData(unittest.TestCase):
    def test_getProfileData_1(self):
        MyProfiledata = [1,'rohit.gs28@gmail.com','Rohit','Gollarahalli','1333,South park street', ' ','B3J2K9','','Halifax','Nova Scotia','Canada',
        '902-989-4524','I like to read','Healthasyst','2014-02-01','2017-02-01','','','','Dalhousie University','2017-09-01','2018-09-01','Visvesaraya Technological University','2010-09-01','2014-09-01',
        'HTML','CSS','PYTHON','OOPS','Stock price','Predictor model!This project predicts stock prices','Chatbot which identifies depression','Used by different health professionals','','','employee','plan1']
        mockObject = FetchMyUserData.FetchMyUserData('rohit.gs28@gmail.com',MyProfiledata,'pass')
        mockObject.getProfileData = MagicMock(return_value=Profiledata)
        mockObject.getProfileData("rohit.gs28@gmail.com")
        assert mockObject.getProfileData("rohit.gs28@gmail.com") == MyProfiledata

    def test_getProfileData_2(self):
        MyProfiledata = [1,'rohit.gs28@gmail.com','Rohit','Gollarahalli','1333,South park street', ' ','B3J2K9','','Halifax','Nova Scotia','Canada',
        '902-989-4524','I like to read','Healthasyst','2014-02-01','2017-02-01','','','','Dalhousie University','2017-09-01','2018-09-01','Visvesaraya Technological University','2010-09-01','2014-09-01',
        'HTML','CSS','PYTHON','OOPS','Stock price','Predictor model!This project predicts stock prices','Chatbot which identifies depression','Used by different health professionals','','','employee','plan1']
        mockObject = FetchMyUserData.FetchMyUserData('rohit.gs28@gmail.com',MyProfiledata,'pass')
        mockObject.getProfileData = MagicMock(return_value=Profiledata)
        mockObject.getProfileData("rohit.gs28@gmail.com")
        mockObject.getProfileData.assert_called_with("rohit.gs28@gmail.com")


if __name__ == '__main__':
    unittest.main()
