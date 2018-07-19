import hashlib, os
import logging
from abc import ABCMeta, abstractmethod
#from extensions import mysql

class ICheckValidity:
    @abstractmethod
    def isValid_DBL(Self,email, password): raise NotImplementedError
