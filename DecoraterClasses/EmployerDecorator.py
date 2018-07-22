from User import User

class EmployerDecorator(User):
    def __init__(self, user):
        self.user = user

    def plan_rules(self):
        print "This is Employer class"
