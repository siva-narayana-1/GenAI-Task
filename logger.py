import sys
import logging
import os

class Logger:
    def get_logs(log_name):
        try:

            logger = logging.getLogger(log_name)
            logger.setLevel(logging.DEBUG)

            if not os.path.exists("./Logs"):
                os.makedirs("./Logs")
                handler = logging.FileHandler(f'./Logs/{log_name}.log')

            handler = logging.FileHandler(f'./Logs/{log_name}.log')
            formate = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            handler.setFormatter(formate)
            logger.addHandler(handler)

            return logger
        except Exception as e:
            exc_type, exc_msg, exc_line = sys.exc_info()

            print(f'{exc_type} at {exc_line.tb_lineno} as {exc_msg}')


