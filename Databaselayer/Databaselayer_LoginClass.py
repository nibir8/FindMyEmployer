import hashlib, os
import logging
from extensions import mysql
import IFetchLoginDetails
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class Databaselayer_LoginClass(IFetchLoginDetails.IFetchLoginDetails):
    def getLoginDetails_DBL(self,email):
        try:
            loggedIn = True
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetUserDetails',[email])
            userId, firstName = cur.fetchone()
        except Exception as e:
            excep_msg = "Error occured in getLoginDetails_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return (loggedIn, firstName)
