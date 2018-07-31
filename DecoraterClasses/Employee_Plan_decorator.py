from EmployeeDecorator import EmployeeDecorator

class Employee_Plan_decorator(EmployeeDecorator):
  def __init__(self, employee):
      super(Employee_Plan_decorator, self).__init__(employee)

  def plan_rules(self,givenCount,userCount,messagePermission):
      allow = False
      givenCount = int(givenCount)
      userCount = int(userCount)
      if givenCount>userCount:
        allow = True
      elif givenCount<=userCount:
        allow = False
      return allow,messagePermission
