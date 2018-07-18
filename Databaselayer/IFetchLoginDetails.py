import hashlib, os
import logging

class IFetchLoginDetails:
    def getLoginDetails_DBL(self,email): raise NotImplementedError
