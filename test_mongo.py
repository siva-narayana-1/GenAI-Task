from pymongo import MongoClient
import sys
from logger import Logger
log = Logger.get_logs("test_mongoDB")

class Connecction_db:
    def __init__(self):
        self.collection = None
        self.db = None
        self.connect = None

    def db_connect(self):
        try:
            self.connect = MongoClient("mongodb://localhost:27017")
            if self.connect:
                self.db = self.connect["clg_db"]
                self.collection = self.db["students"]

                log.info("Sucessfully collection checked..")
                data = list(self.collection.find_one({"year":2}))
                log.info(data)

            else:
                log.info("Problem with host link....")
        except:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.info(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")

        finally:
            if self.connect:
                self.connect.close()

if __name__ == "__main__":
    obj = Connecction_db()
    obj.db_connect()