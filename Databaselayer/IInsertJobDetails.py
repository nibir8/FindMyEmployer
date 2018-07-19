import hashlib, os
import logging  

class IInsertJobDetails:
    def insertJob_DBL(Self,jobId,companyName,title,manager,location,jobDetails): raise NotImplementedError
