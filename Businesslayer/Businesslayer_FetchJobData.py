import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_FetchJob import Databaselayer_FetchJob

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_FetchJobData:
    def getJobData_BSL(self):
        try:
            fetchjobdata = Databaselayer_FetchJob()
            jobData = fetchjobdata.getJob_DBL()
            return jobData
        except Exception as e:
            excep_msg = "Error occured in method getJobData_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
