import hashlib, os
import logging

class IPostStatus:
    def insertUserStatus(self): raise NotImplementedError
    def getUserStatuses(self): raise NotImplementedError
