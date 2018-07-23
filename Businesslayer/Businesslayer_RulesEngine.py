import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_UpdateMyProfile import Databaselayer_UpdateMyProfile
from Databaselayer_FetchApplicationCount import Databaselayer_FetchApplicationCount
from Databaselayer_FetchJobsCount import Databaselayer_FetchJobsCount

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

sys.path.append(os.path.abspath(os.path.join('0', '../DecoraterClasses')))
from NormalEmployee import NormalEmployee
from Employee_Plan1_decorator import Employee_Plan1_decorator
from Employee_Plan2_decorator import Employee_Plan2_decorator
from NormalEmployer import NormalEmployer
from Employer_Plan1_decorator import Employer_Plan1_decorator
from Employer_Plan2_decorator import Employer_Plan2_decorator

class Businesslayer_RulesEngine:

    def rulesEngine_Employee_BSL(self,email,typeOfPlan):
        try:
            fetchApplicationCount = Databaselayer_FetchApplicationCount()
            applicationcount = fetchApplicationCount.getApplicationCount_DBL(email)
            print applicationcount
            concreteComponent =  NormalEmployee()
            concrete_decorator_planA =  Employee_Plan1_decorator(concreteComponent)
            concrete_decorator_planB =  Employer_Plan2_decorator(concrete_decorator_planA)
            if typeOfPlan == "plan1":
                allowPosting = concrete_decorator_planA.plan_rules(applicationcount)
            elif typeOfPlan == "plan2":
                allowPosting = concrete_decorator_planB.plan_rules(applicationcount)

            return allowPosting
        except Exception as e:
            excep_msg = "Error occured in method rulesEngine_Employee_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)

    def rulesEngine_Employer_BSL(self,email,typeOfPlan):
        try:
            print "This"
            print email
            print typeOfPlan
            fetchJobsCount = Databaselayer_FetchJobsCount()
            jobsCount  = fetchJobsCount.getJobsCount_DBL(email)
            concreteComponent = NormalEmployer()
            concrete_decorator_planA = Employer_Plan1_decorator(concreteComponent)
            concrete_decorator_planB = Employer_Plan2_decorator(concrete_decorator_planA)
            if typeOfPlan == "plan1":
                allowPosting = concrete_decorator_planA.plan_rules(jobsCount)
            elif typeOfPlan == "plan2":
                allowPosting = concrete_decorator_planB.plan_rules(jobsCount)
            return allowPosting
        except Exception as e:
            excep_msg = "Error occured in method rulesEngine_Employer_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
