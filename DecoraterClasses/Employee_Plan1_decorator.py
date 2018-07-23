from EmployeeDecorator import EmployeeDecorator

class Employee_Plan1_decorator(EmployeeDecorator):
  def __init__(self, employee):
      super(Employee_Plan1_decorator, self).__init__(employee)

  def plan_rules(self,givenCount):
      plan1Count= 5
      allow = False
      if givenCount<=plan1Count:
        allow = True
      elif givenCount>plan1Count:
        allow = False
      return allow
