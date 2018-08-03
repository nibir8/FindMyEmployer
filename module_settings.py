import os
import sys,os
import time
import hashlib
import glob
from werkzeug.utils import secure_filename
import os.path
from flask_mail import Mail, Message
from flask import Flask, render_template, redirect, url_for, request, session
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import logging
from shutil import copyfile

sys.path.append(os.path.abspath(os.path.join('0','/Businesslayer')))

from Businesslayer import UpdateMyUserobject
from Businesslayer import HashMyChangingPassword
from Businesslayer import CheckIfMyUserValid
from Businesslayer import FetchMyJobData
from Businesslayer import FetchMySearchedProfile
from Businesslayer import FetchAllUserStatuses
from Businesslayer import InsertUserJob
from Businesslayer import InsertMyUser
from Businesslayer import LoginMyClass
from Businesslayer import PostUserStatus
from Businesslayer import UpdateMyGivenProfile
from Businesslayer import GetMyUserType
from Businesslayer import Email_NullCheck
from Businesslayer import Password_NullCheck
from Businesslayer import Email_Validate
from Businesslayer import FirstName_SpaceCheck
from Businesslayer import Password_Equate
from Businesslayer import Password_SpaceCheck
from Businesslayer import RulesEngine_PlanType
from Businesslayer import InsertGivenJobApplication
from Businesslayer import FetchMyUserData
from Businesslayer import FactoryPattern
from Businesslayer import XmlReader

sys.path.append(os.path.abspath(os.path.join('0','../Models')))
from MyUser import MyUser
sys.path.append(os.path.abspath(os.path.join('0','../extensions')))
from extensions import mysql
from extensions_logging import logmyerror
from extensionsUser import myUser
from CaptureSessionid import CaptureSessionid
from extensionCaptureSessionId import captureSessionid
