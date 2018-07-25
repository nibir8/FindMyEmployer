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

from Businesslayer import Businesslayer_UpdateMyobject
from Businesslayer import Businesslayer_ChangeMyPassword
from Businesslayer import Businesslayer_CheckIfUserValid
from Businesslayer import Businesslayer_FetchJobData
from Businesslayer import Businesslayer_FetchSearchedProfile
from Businesslayer import Businesslayer_GetStatus
from Businesslayer import Businesslayer_InsertJob
from Businesslayer import Businesslayer_InsertUser
from Businesslayer import Businesslayer_LoginClass
from Businesslayer import Businesslayer_PostStatus
from Businesslayer import Businesslayer_UpdateMyProfile
from Businesslayer import Businesslayer_GetUserType
from Businesslayer import Businesslayer_Validator_Email_NullCheck
from Businesslayer import Businesslayer_Validator_Pass_NullCheck
from Businesslayer import Businesslayer_Validator_Email_Validate
from Businesslayer import Businesslayer_Validator_FirstName_SpaceCheck
from Businesslayer import Businesslayer_Validator_Password_Equate
from Businesslayer import Businesslayer_Validator_Password_SpaceCheck
from Businesslayer import Businesslayer_RulesEngine
from Businesslayer import Businesslayer_InsertJobApplication
from Businesslayer import Businesslayer_FetchUserData
from Businesslayer import Businesslayer_FactoryPattern

sys.path.append(os.path.abspath(os.path.join('0','../Models')))
from MyUser import MyUser
sys.path.append(os.path.abspath(os.path.join('0','../extensions')))
from extensions import mysql
from extensions_logging import logmyerror
from extensionsUser import myUser
from CaptureSessionid import CaptureSessionid
from extensionCaptureSessionId import captureSessionid
