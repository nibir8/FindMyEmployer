import os.path
import logging
import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_FetchStatus import Databaselayer_FetchStatus

class Businesslayer_GetStatus:
    def getUserStatus_BSL(Self):
        try:

            fetchuserStatus = Databaselayer_FetchStatus()
            statusData  = fetchuserStatus.getUserStatus_DBL()
            return statusData
        except:
            msg = "Error occured in method getJobData_BSL method"
            logging.info(msg, exc_info=True)
