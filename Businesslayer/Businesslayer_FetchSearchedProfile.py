import os.path
import logging

import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_FetchSearchedProfile import Databaselayer_FetchSearchedProfile

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror

class Businesslayer_FetchSearchedProfile:
    def fetchSearchedProfile_BSL(self,firstName):
        try:
            fetchSearchedProfile = Databaselayer_FetchSearchedProfile()
            fetchSearchedProfileData = fetchSearchedProfile.fetchSearchedProfile_DBL(firstName)
            return fetchSearchedProfileData
        except Exception as e:
            excep_msg = "Error occured in method fetchSearchedProfile_BSL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
