#!/usr/bin/python

import unittest
from xml.dom.minidom import parse
import xml.dom.minidom
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from glob import glob
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


class Businesslayer_XmlReader:
    def readmyFile(self,UserType):
        try:
            Employees = []
            Employers = []
            EmployeePlans = []
            EmployerPlans = []

            EmployeePlanName = []
            EmployeePlanCount = []
            EmployeePlanPrice = []

            EmployerPlanName = []
            EmployerPlanCount = []
            EmployerPlanPrice = []
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
                EmployeePlanName.append(givenName)
                EmployeePlanPrice.append(givenPrice)
                EmployeePlanCount.append(givenCount)


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
                EmployerPlanName.append(givenName)
                EmployerPlanPrice.append(givenPrice)
                EmployerPlanCount.append(givenCount)
            if UserType =='employee':
                return EmployeePlanName,EmployeePlanCount,EmployeePlanPrice
            elif UserType =='employer':
                return EmployerPlanName,EmployerPlanCount,EmployerPlanPrice

        except Exception, e:
            print "Exception"
            print "%s is NOT well-formed! %s" % (filename, e)
