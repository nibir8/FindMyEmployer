import unittest
import mock
from mock import MagicMock,patch
import os.path
import logging
import sys,os
from MockData import User_Details_list
import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..','Models/')))
import MyUser

sys.path.append(os.path.abspath(os.path.join('..', 'extensions/')))
import extensions
sys.path.append(os.path.abspath(os.path.join('..', 'LoggingDatabase/')))
import LoggingErrorsinDatabase
sys.path.append(os.path.abspath(os.path.join('..', 'Businesslayer/')))
import Businesslayer_UpdateMyobject


class Businesslayer_UpdateMyobject_Test(unittest.TestCase):
    def test_updateMyObjectBSL_1(self):
        mockObject = Businesslayer_UpdateMyobject.Businesslayer_UpdateMyobject()
        mockObject.updateMyObjectBSL = MagicMock(return_value="User Successfully Registered")
        mockObject.updateMyObjectBSL("a@a.a","123","Nibir","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada",User_Details_list,"Employee","plan1")
        assert mockObject.updateMyObjectBSL("a@a.a","123","Nibir","Mukherjee","1333","South","B3J 2K9","Halifax","NS","Canada",User_Details_list,"Employee","plan1") == "User Successfully Registered"

    def test_updateMyObjectBSL_BSL_2(self):
        mockObject = Businesslayer_UpdateMyobject.Businesslayer_UpdateMyobject()
        mockObject.updateMyObjectBSL = MagicMock(return_value="User Registration Failed")
        mockObject.updateMyObjectBSL("a@a.a","123","Nibir","","1333","South","","Halifax","NS","Canada",User_Details_list,"Employee","plan1")
        assert mockObject.updateMyObjectBSL("a@a.a","123","Nibir","","1333","South","","Halifax","NS","Canada",User_Details_list,"Employee","plan1") == "User Registration Failed"

if __name__ == '__main__':
    unittest.main()
