from EmployeeDecorator import EmployeeDecorator

class Employee_Plan2_decorator(EmployeeDecorator):


  def __init__(self, user):
      super(Employee_Plan2_decorator, self).__init__(user)

  def plan_rules(self,givenCount):
      print "This is for plan 2 for Employee 1"
      plan2Count= 30
      allow = False
      if givenCount<=plan2Count:
        allow = True
      elif givenCount>plan2Count:
        allow = False
      return allow
