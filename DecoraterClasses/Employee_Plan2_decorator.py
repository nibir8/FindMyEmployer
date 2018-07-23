from EmployeeDecorator import EmployeeDecorator

class Employee_Plan2_decorator(EmployeeDecorator):


  def __init__(self, employee):
      super(Employee_Plan2_decorator, self).__init__(employee)

  def plan_rules(self,givenCount):
      plan2Count= 30
      allow = False
      if givenCount<=plan2Count:
        allow = True
      elif givenCount>plan2Count:
        allow = False
      return allow
