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
import FetchGetApplicationCount
from FetchJobsCount import FetchJobsCount
sys.path.append(os.path.abspath(os.path.join('..', 'DecoraterClasses/')))
from NormalEmployee import NormalEmployee
from Employee_Plan_decorator import Employee_Plan_decorator
from NormalEmployer import NormalEmployer
from Employer_Plan_decorator import Employer_Plan_decorator

sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import RulesEngine_PlanType
import XmlReader

class Test_RulesEngine_PlanType(unittest.TestCase):
    def test_rulesEngine_Employee_1(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(13)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employee('rohit.gs28@gmail.com','employee','plan1')
        assert allowPosting == False
        assert allowMessagePermission == False


    def test_rulesEngine_Employee_2(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(5)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employee('rohit.gs28@gmail.com','employee','plan1')
        assert allowPosting == True
        assert allowMessagePermission == False

    def test_rulesEngine_Employee_3(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(13)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employee('rohit.gs28@gmail.com','employee','plan2')
        assert allowPosting == True
        assert allowMessagePermission == True

    def test_rulesEngine_Employee_4(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(50)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employee('rohit.gs28@gmail.com','employee','plan2')
        assert allowPosting == False
        assert allowMessagePermission == True


    def test_rulesEngine_Employer_1(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(15)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employer('rohit.gs28@gmail.com','employer','plan1')
        assert allowPosting == False
        assert allowMessagePermission == False


    def test_rulesEngine_Employer_2(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(3)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employer('rohit.gs28@gmail.com','employer','plan1')
        assert allowPosting == True
        assert allowMessagePermission == False

    def test_rulesEngine_Employer_3(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(15)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employer('rohit.gs28@gmail.com','employer','plan2')
        assert allowPosting == True
        assert allowMessagePermission == True

    def test_rulesEngine_Employer_4(self):
        rulesEngine_PlanType = RulesEngine_PlanType.RulesEngine_PlanType(50)
        allowPosting,allowMessagePermission = rulesEngine_PlanType.rulesEngine_Employer('rohit.gs28@gmail.com','employer','plan2')
        assert allowPosting == False
        assert allowMessagePermission == True




if __name__ == '__main__':
    unittest.main()
