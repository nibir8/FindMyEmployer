import hashlib, os
import logging
from extensions import mysql
import IFetchSearchedProfile
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror


class Databaselayer_FetchSearchedProfile(IFetchSearchedProfile.IFetchSearchedProfile):
    def fetchSearchedProfile_DBL(self,firstName):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.callproc('spGetSearchedUser',[firstName])
            searchedProfileData = cur.fetchall()
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in fetchSearchedProfile_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        return searchedProfileData
