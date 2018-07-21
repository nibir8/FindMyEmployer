import os,sys
sys.path.append(os.path.abspath(os.path.join('0','../Models')))
from User import User
from Employee import Employee
from Employer import Employer
userlist= []
employeeUserlist=[]
employerUserlist=[]
myUser = User('','','','','','','','','','','','','',userlist)
myEmployee = Employee('','','','','','','','','','','','','',employeeUserlist)
myEmployer = Employer('','','','','','','','','','','','','',employerUserlist)
#myuser = User()
