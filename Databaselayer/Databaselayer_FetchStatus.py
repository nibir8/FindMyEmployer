import hashlib, os
import logging
from extensions import mysql
import IPostStatus
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class Databaselayer_FetchStatus(IPostStatus.IPostStatus):
    def getUserStatus_DBL(Self):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetUserStatus')
            statusData = cur.fetchall()
            #print statusData
            conn.commit()
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getProfileData_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return statusData