from EmployerDecorator import EmployerDecorator


class Employer__Plan2_decorator(EmployerDecorator):
  def __init__(self, employerDecorator):
      self.employerDecorator = employerDecorator

  def settings():
      print "This is for plan 1"
