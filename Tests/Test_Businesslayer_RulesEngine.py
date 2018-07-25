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
from Databaselayer_UpdateMyProfile import Databaselayer_UpdateMyProfile
from Databaselayer_FetchApplicationCount import Databaselayer_FetchApplicationCount
from Databaselayer_FetchJobsCount import Databaselayer_FetchJobsCount
sys.path.append(os.path.abspath(os.path.join('..', 'DecoraterClasses/')))
from NormalEmployee import NormalEmployee
from Employee_Plan1_decorator import Employee_Plan1_decorator
from Employee_Plan2_decorator import Employee_Plan2_decorator
from NormalEmployer import NormalEmployer
from Employer_Plan1_decorator import Employer_Plan1_decorator
from Employer_Plan2_decorator import Employer_Plan2_decorator

sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_RulesEngine

class Businesslayer_RulesEngine_Test(unittest.TestCase):
    def test_rulesEngine_Employee_BSL_1(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employee_BSL = MagicMock(return_value=True)
        mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1")
        assert mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1") == True

    def test_rulesEngine_Employee_BSL_2(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employee_BSL = MagicMock(return_value=False)
        mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1")
        assert mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1") == False

    def test_rulesEngine_Employee_BSL_3(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employee_BSL = MagicMock(return_value=True)
        mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1")
        assert mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1") == True

    def test_rulesEngine_Employee_BSL_4(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employee_BSL = MagicMock(return_value=False)
        mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1")
        assert mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1") == False

    def test_rulesEngine_Employee_BSL_5(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employee_BSL = MagicMock(return_value=False)
        mockObject.rulesEngine_Employee_BSL("rohit.gs28@gmail.com","Plan1")
        mockObject.rulesEngine_Employee_BSL.assert_called_with("rohit.gs28@gmail.com", "Plan1")

    def test_rulesEngine_Employer_BSL_1(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employer_BSL = MagicMock(return_value=True)
        mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan1")
        assert mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan1") == True


    def test_rulesEngine_Employer_BSL_2(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employer_BSL = MagicMock(return_value=False)
        mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan1")
        assert mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan1") == False

    def test_rulesEngine_Employer_BSL_3(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employer_BSL = MagicMock(return_value=True)
        mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan2")
        assert mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan2") == True

    def test_rulesEngine_Employer_BSL_4(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employer_BSL = MagicMock(return_value=False)
        mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan2")
        assert mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan2") == False

    def test_rulesEngine_Employer_BSL_5(self):
        mockObject = Businesslayer_RulesEngine.Businesslayer_RulesEngine()
        mockObject.rulesEngine_Employer_BSL = MagicMock(return_value=True)
        mockObject.rulesEngine_Employer_BSL("rohit.gollarahalli@dal.ca","Plan1")
        mockObject.rulesEngine_Employer_BSL.assert_called_with("rohit.gollarahalli@dal.ca", "Plan1")




if __name__ == '__main__':
    unittest.main()
