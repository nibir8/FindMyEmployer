import os.path
import logging
import sys
sys.path.append(os.path.abspath(os.path.join('0','../Databaselayer')))
from PostMyStatus import PostMyStatus

sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions_logging import logmyerror
from extensions import mysql

class PostUserStatus:

        def __init__(self,email,status,msg):
            self.email = email
            self.status = status
            self.finalMessage = msg

        def set_messages(self,argument):
            return{
                'pass': 'Successfully posted status',
                'fail': 'Could not post status'
            }.get(argument, 'Could not post status')
        def insertUserStatus(self):
            try:
                if self.finalMessage == "":
                    databaselayerupdatestatus = PostMyStatus(mysql,self.email,self.status,'')
                    result = databaselayerupdatestatus.insertMyUserStatus()
                    self.finalMessage = self.set_messages(result)
                return self.finalMessage
            except Exception as e:
                excep_msg = "Error occured in method insertUserStatus_BSL method"
                level = logging.getLogger().getEffectiveLevel()
                logmyerror.loadMyExceptionInDb(level,excep_msg,e)
                logging.info(excep_msg, exc_info=True)
