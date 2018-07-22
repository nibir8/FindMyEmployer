from EmployeeDecorator import EmployeeDecorator

class Employee_Plan1_decorator(EmployeeDecorator):


  def __init__(self,employeeDecorator):
      self.employeeDecorator = employeeDecorator

  def settings(self):
      print "This is for plan 2 for Employee 1"
