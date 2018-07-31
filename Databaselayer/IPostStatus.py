import hashlib, os
import logging

class IPostStatus:
    def insertUserStatus(Self,email,status): raise NotImplementedError
    def getUserStatuses(Self): raise NotImplementedError
