import os.path
import logging

import sys

sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from Databaselayer_FetchSearchedProfile import Databaselayer_FetchSearchedProfile

class Businesslayer_FetchSearchedProfile:
    def fetchSearchedProfile_BSL(self,firstName):
        try:
            fetchSearchedProfile = Databaselayer_FetchSearchedProfile()
            fetchSearchedProfileData = fetchSearchedProfile.fetchSearchedProfile_DBL(firstName)
            return fetchSearchedProfileData
        except:
            msg = "Error occured in method fetchSearchedProfile_BSL method"
            logging.info(msg, exc_info=True)
