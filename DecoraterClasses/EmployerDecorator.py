from Employer import Employer

class EmployerDecorator(Employer):
    def __init__(self, employer):
        self.employer = employer

    def plan_rules(self,givenCount,userCount,messagePermission):
        return "This is Employer class"
