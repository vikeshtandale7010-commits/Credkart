import logging

class log_generator_class:

    @staticmethod
    def log_gen_method():
        log_file = logging.FileHandler(".\\Logs\\CredKart.log") # log file
        # 2024-08-08 09:12:24,712 : INFO : test_Signup_002  : Opening browser
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s') # log format
        log_file.setFormatter(log_format) # log file --> log format
        logger = logging.getLogger() # getLogger object
        logger.addHandler(log_file) #  add new log everytime in same log file
        logger.setLevel(logging.INFO) # Level set
        return logger


"""
log level : 

debug
info
warning
error
critical

"""