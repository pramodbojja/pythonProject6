import inspect
import logging
class BaseClass:
    def test_logs(self):

        logger_name = inspect.stack()[1][1] #need to know more about it
        logger = logging.getLogger(logger_name)
        fileHandler = logging.FileHandler("logging.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.error("error")
        logger.warning("Something is in warning mode")
        logger.critical("Critical issue")
        return logger

"""    
class BaseClass:
    def test_logs(self):
        logger_name = inspect.stack()[1][1]
        logger = logging.getLogger(logger_name)

        logging.basicConfig(filename="loginfile.log",
                            format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                            datefmt='%m/%d/%y %I:%M:%S:%p',
                            level=logging.DEBUG)

        logger.setLevel(logging.DEBUG)
        logger.debug("A debug statement is executed ")
        logger.info("Information")
        logger.warning("something is in warning mode")
        logger.error("An error has occured")
        logger.critical("Critical issue")
        return logger
        
        
    def gettestlogers(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        fileHandler = logging.FileHandler(filename="freshlog.log", mode="a")
       # filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.log')
       # logging.basicConfig(filename=filename, level=logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # logger.debug("A debug statement is executed ")
        # logger.info("Information")
        # logger.warning("something is in warning mode")
        # logger.error("An error has occured")
        # logger.critical("Critical issue")
        return logger

        """
