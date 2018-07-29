import os.path
import logging
import sys
from Businesslayer_XmlReader import Businesslayer_XmlReader
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_UpdateMyProfile import Databaselayer_UpdateMyProfile
from Databaselayer_FetchApplicationCount import Databaselayer_FetchApplicationCount
from Databaselayer_FetchJobsCount import Databaselayer_FetchJobsCount

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

sys.path.append(os.path.abspath(os.path.join('0', '../DecoraterClasses')))
from NormalEmployee import NormalEmployee
from Employee_Plan_decorator import Employee_Plan_decorator
from NormalEmployer import NormalEmployer
from Employer_Plan_decorator import Employer_Plan_decorator

class Businesslayer_RulesEngine:

    def rulesEngine_Employee_BSL(self,email,UserType,typeOfPlan):
        try:
            reader = Businesslayer_XmlReader()
            EmployeePlanName,EmployeePlanCount,EmployeePlanPrice = reader.readmyFile(UserType)
            fetchApplicationCount = Databaselayer_FetchApplicationCount()
            applicationcount = fetchApplicationCount.getApplicationCount_DBL(email)
            concreteComponent =  NormalEmployee()
            concrete_decorator_plan =  Employee_Plan_decorator(concreteComponent)
            for index, item in enumerate(EmployeePlanName):
                if typeOfPlan == item:
                    allowPosting = concrete_decorator_plan.plan_rules(EmployeePlanCount[index],applicationcount)
            return allowPosting
        except Exception as e:
            excep_msg = "Error occured in method rulesEngine_Employee_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)

    def rulesEngine_Employer_BSL(self,email,UserType,typeOfPlan):
        try:
            reader = Businesslayer_XmlReader()
            EmployerPlanName,EmployerPlanCount,EmployerPlanPrice = reader.readmyFile(UserType)
            fetchJobsCount = Databaselayer_FetchJobsCount()
            jobsCount  = fetchJobsCount.getJobsCount_DBL(email)
            concreteComponent = NormalEmployer()
            concrete_decorator_planA = Employer_Plan_decorator(concreteComponent)
            for index, item in enumerate(EmployerPlanName):
                if typeOfPlan == item:
                    allowPosting = concrete_decorator_planA.plan_rules(EmployerPlanCount[index],fetchJobsCount)
            return allowPosting
        except Exception as e:
            excep_msg = "Error occured in method rulesEngine_Employer_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
