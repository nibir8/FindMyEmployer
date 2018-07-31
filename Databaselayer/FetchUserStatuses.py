import hashlib, os
import logging
from extensions import mysql
import IPostStatus
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class FetchUserStatuses(IPostStatus.IPostStatus):
    def __init__(self,mysql,StatusData,msg):
        self.mysql = mysql
        self.StatusData = StatusData
        self.result = msg

    def getUserStatuses(self):
        try:
            conn = self.mysql.connect()
            cur = conn.cursor()
            if self.result == "":
                cur.callproc('spGetUserStatus')
                self.StatusData = cur.fetchall()
                conn.commit()
                self.result = "pass"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in getUserStatuses method in databaselayer"
            self.result = "fail"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return self.StatusData,self.result
