import os.path
import logging
import sys
from XmlReader import XmlReader
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from FetchJobsCount import FetchJobsCount

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensions import mysql

sys.path.append(os.path.abspath(os.path.join('0', '../DecoraterClasses')))
from NormalEmployee import NormalEmployee
from Employee_Plan_decorator import Employee_Plan_decorator
from NormalEmployer import NormalEmployer
from Employer_Plan_decorator import Employer_Plan_decorator

class RulesEngine_PlanType:
    def __init__(self,count):
        self.count = count

    def rulesEngine_Employee(self,email,UserType,typeOfPlan):
        try:
            reader = XmlReader()
            EmployeePlanName,EmployeePlanCount,EmployeePlanPrice,EmployeeMessagePermission = reader.readmyFile(UserType)
            if self.count == "":
                fetchApplicationCount = FetchGetApplicationCount(mysql,email,'','')
                self.count,result  = fetchApplicationCount.getApplicationCount(email)
            concreteComponent =  NormalEmployee()
            concrete_decorator_plan =  Employee_Plan_decorator(concreteComponent)
            for index, item in enumerate(EmployeePlanName):
                if typeOfPlan == item:
                    allowPosting,allowMessagePermission = concrete_decorator_plan.plan_rules(EmployeePlanCount[index],self.count,EmployeeMessagePermission[index])
            return allowPosting,allowMessagePermission
        except Exception as e:
            excep_msg = "Error occured in method rulesEngine_Employee_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)

    def rulesEngine_Employer(self,email,UserType,typeOfPlan):
        try:
            reader = XmlReader()
            EmployerPlanName,EmployerPlanCount,EmployerPlanPrice,EmployerMessagePermission = reader.readmyFile(UserType)
            if self.count == "":
                fetchJobsCount = FetchJobsCount(mysql,email,'','')
                self.count,result  = fetchJobsCount.getJobsCount()
            concreteComponent = NormalEmployer()
            concrete_decorator_planA = Employer_Plan_decorator(concreteComponent)
            for index, item in enumerate(EmployerPlanName):
                if typeOfPlan == item:
                    allowPosting,allowMessagePermission = concrete_decorator_planA.plan_rules(EmployerPlanCount[index],self.count,EmployerMessagePermission[index])
            return allowPosting,allowMessagePermission
        except Exception as e:
            excep_msg = "Error occured in method rulesEngine_Employer_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
