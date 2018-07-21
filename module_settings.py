import os
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
from Businesslayer import Businesslayer_ChangeMyPassword
from Businesslayer import Businesslayer_CheckIfUserValid
from Businesslayer import Businesslayer_FetchJobData
from Businesslayer import Businesslayer_FetchSearchedProfile
from Businesslayer import Businesslayer_FetchUserData
from Businesslayer import Businesslayer_GetStatus
from Businesslayer import Businesslayer_InsertJob
from Businesslayer import Businesslayer_InsertUser
from Businesslayer import Businesslayer_LoginClass
from Businesslayer import Businesslayer_PostStatus
from Businesslayer import Businesslayer_UpdateMyProfile
from Businesslayer import Businesslayer_GetUserType
from Businesslayer import Businesslayer_Validator
from shutil import copyfile
import sys,os
sys.path.append(os.path.abspath(os.path.join('0','/extensions')))
from extensions import mysql
from extensions_logging import logmyerror
