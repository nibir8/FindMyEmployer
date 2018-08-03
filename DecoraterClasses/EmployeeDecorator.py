from Employee import Employee

class EmployeeDecorator(Employee):
    def __init__(self, employee):
        self.employee = employee

    def plan_rules(self,givenCount,userCount,messagePermission):
        return "This is Employee class"
