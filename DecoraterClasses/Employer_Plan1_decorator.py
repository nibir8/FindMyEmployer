from EmployerDecorator import EmployerDecorator


class Employer_Plan1_decorator(EmployerDecorator):
  def __init__(self, employer):
      super(Employer_Plan1_decorator, self).__init__(employer)

  def plan_rules(self,givenCount):
      plan1Count= 5
      allow = False
      if givenCount<=plan1Count:
        allow = True
      elif givenCount>plan1Count:
        allow = False
      return allow
