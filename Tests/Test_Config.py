from flask import Flask
from flaskext.mysql import MySQL
import unittest
from extensions_test import mysql
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
mysql.init_app(app)
