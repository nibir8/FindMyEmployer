import hashlib, os
import logging
import ICheckValidity
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror

class Databaselayer_CheckIfUserValid(ICheckValidity.ICheckValidity):
    def isValid_DBL(Self,email, password):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetAllUsers')
            data = cur.fetchall()
            conn.close()
        except Exception as e:
            excep_msg = "Error occured in isValid_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        for row in data:
            if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
                return True
        return False
