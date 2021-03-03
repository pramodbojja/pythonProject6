import logging

def test_logs():
    logger = logging.getLogger(__name__)
    fileHandler =logging.FileHandler("logging.log")
    formatter =logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)


    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.error("error")
    logger.warning("Something is in warning mode")
    logger.critical("Critical issue")

#comments:Full process step by step
#SUMMARY: 1. Create a file name called test_loggingPractise.py
#2. import logging method
#3. create logger.debug, info,warning,error,critical methods
#4. create a file called logger.log using logging.Filehandler method n pass file name
#5. need to format file using using logging.formatter(pass time , level, name and message ) name this as formatter
#6. you need to set the format again using logging.setformat(pass in formatter)
#7.logger.addhandler (pass filehadler here)
#8 set level using logger.setLevel(logging.INFO)