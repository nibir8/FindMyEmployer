from Employee import Employee

class EmployeeDecorator(Employee):
    def __init__(self, employee):
        self.employee = employee

    def plan_rules(self):
        print "This is Employee class"
