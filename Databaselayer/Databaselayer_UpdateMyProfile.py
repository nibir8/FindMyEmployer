import hashlib, os
import logging
import IProfileUpdate
import sys
sys.path.append(os.path.abspath(os.path.join('0', '../extensions')))
from extensions import mysql
from extensions_logging import logmyerror



class Databaselayer_UpdateMyProfile(IProfileUpdate.IProfileUpdate):
    def updateMyProfileMethod_DBL(Self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details_list):
        try:
            msg=""
            conn = mysql.connect()
            cur = conn.cursor()
            logging.info("Creating a new database connection")
            cur.callproc('spUpdateUser',[email,firstName,lastName,address1,address2,city,zipcode,state,country,phone,
            user_details_list[0],user_details_list[1],user_details_list[2],user_details_list[3],
            user_details_list[4],user_details_list[5],user_details_list[6],
            user_details_list[7],user_details_list[8],user_details_list[9],user_details_list[10],
            user_details_list[11],user_details_list[12],user_details_list[13],user_details_list[14],
            user_details_list[15],user_details_list[16],user_details_list[17],user_details_list[18],
            user_details_list[19],user_details_list[20],user_details_list[21],user_details_list[22]])
            conn.commit()
            logging.info("Changes updated in the database")
            msg = "Saved Successfully"
        except Exception as e:
            conn.rollback()
            excep_msg = "Error occured in changeMyProfilePassword_DBL method"
            level = logging.getLogger().getEffectiveLevel()
            logmyerror.loadMyExceptionInDb(level,excep_msg,e)
            logging.info(excep_msg, exc_info=True)
        conn.close()
        logging.info("Closing database connection")
        return msg