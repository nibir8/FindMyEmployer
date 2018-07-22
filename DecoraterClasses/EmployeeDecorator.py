from User import User

class EmployeeDecorator(User):
    def __init__(self, user):
        self.User = user

    def plan_rules(self):
        print "This is Employee class"
