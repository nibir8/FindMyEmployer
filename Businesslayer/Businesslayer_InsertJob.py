import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_InsertJob import Databaselayer_InsertJob

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_InsertJob:
    def insertJob_BSL(self,jobId,companyName,title,manager,location,jobDetails):
        try:
            insertjob = Databaselayer_InsertJob()
            msg = insertjob.insertJob_DBL(jobId,companyName,title,manager,location,jobDetails)
        except Exception as e:
            excep_msg = "Error occured in method insertJob_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        return msg
