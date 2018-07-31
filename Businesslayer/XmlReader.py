#!/usr/bin/python

import unittest
from xml.dom.minidom import parse
import xml.dom.minidom
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import logging
from glob import glob
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror


class XmlReader:

    def set_messagepermission(self,argument):
        if argument =='allow':
            return True
        elif argument =='deny':
            return False


    def readmyFile(self,UserType):
        try:
            Employees = []
            Employers = []
            EmployeePlans = []
            EmployerPlans = []

            EmployeePlanName = []
            EmployeePlanCount = []
            EmployeePlanPrice = []
            EmployeeMessagePermission = []

            EmployerPlanName = []
            EmployerPlanCount = []
            EmployerPlanPrice = []
            EmployerMessagePermission =[]
            filename=dir_path + "/parse.xml"
            parser = make_parser()
            parser.setContentHandler(ContentHandler())
            parser.parse(filename)

            DOMTree = xml.dom.minidom.parse(dir_path + "/parse.xml")
            Employees = DOMTree.getElementsByTagName("Employee")
            Employers = DOMTree.getElementsByTagName("Employer")

            for item in Employees:
                EmployeePlans = item.getElementsByTagName("EmployeePlan")

            for item in Employers:
                EmployerPlans = item.getElementsByTagName("EmployerPlan")

            for plan in EmployeePlans:
                name = plan.getElementsByTagName("Name")[0]
                if not name.childNodes:
                    givenName = ""
                else:
                    givenName = "%s" % name.childNodes[0].data
                Price = plan.getElementsByTagName("Price")[0]
                if not plan.childNodes:
                    givenPrice = ""
                else:
                    givenPrice= "%s" % Price.childNodes[0].data
                Count = plan.getElementsByTagName("Count")[0]
                if not plan.childNodes:
                    givenCount = ""
                else:
                    givenCount =  "%s" % Count.childNodes[0].data
                Messages = plan.getElementsByTagName("Messages")[0]
                if not plan.childNodes:
                    givenMessagesPermission = ""
                else:
                    givenMessagesPermission =  "%s" % Messages.childNodes[0].data
                EmployeePlanName.append(givenName)
                EmployeePlanPrice.append(givenPrice)
                EmployeePlanCount.append(givenCount)
                EmployeeMessagePermission.append(givenMessagesPermission)
            for index,item in enumerate(EmployeeMessagePermission):
                item = self.set_messagepermission(item)
                EmployeeMessagePermission[index] = item


            for plan in EmployerPlans:
                name = plan.getElementsByTagName("Name")[0]
                if not name.childNodes:
                    givenName = ""
                else:
                    givenName = "%s" % name.childNodes[0].data
                Price = plan.getElementsByTagName("Price")[0]
                if not plan.childNodes:
                    givenPrice = ""
                else:
                    givenPrice= "%s" % Price.childNodes[0].data
                Count = plan.getElementsByTagName("Count")[0]
                if not plan.childNodes:
                    givenCount = ""
                else:
                    givenCount =  "%s" % Count.childNodes[0].data
                Messages = plan.getElementsByTagName("Messages")[0]
                if not plan.childNodes:
                    givenMessagesPermission = ""
                else:
                    givenMessagesPermission =  "%s" % Messages.childNodes[0].data
                EmployerPlanName.append(givenName)
                EmployerPlanPrice.append(givenPrice)
                EmployerPlanCount.append(givenCount)
                EmployerMessagePermission.append(givenMessagesPermission)
            for index,item in enumerate(EmployerMessagePermission):
                item = self.set_messagepermission(item)
                EmployerMessagePermission[index] = item


            if UserType =='employee':
                return EmployeePlanName,EmployeePlanCount,EmployeePlanPrice,EmployeeMessagePermission
            elif UserType =='employer':
                return EmployerPlanName,EmployerPlanCount,EmployerPlanPrice,EmployerMessagePermission

        except Exception, e:
            print "Exception"
            print "%s is NOT well-formed! %s" % (filename, e)
            excep_msg = "Error occured in method rulesEngine_Employer_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
