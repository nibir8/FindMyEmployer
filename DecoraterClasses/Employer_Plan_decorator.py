from EmployerDecorator import EmployerDecorator


class Employer_Plan_decorator(EmployerDecorator):
  def __init__(self, employer):
      super(Employer_Plan_decorator, self).__init__(employer)

  def plan_rules(self,givenCount,userCount,messagePermission):
      allow = False
      givenCount = int(givenCount)
      userCount = int(userCount)
      if givenCount>userCount:
        allow = True
      elif givenCount<=userCount:
        allow = False
      return allow,messagePermission
