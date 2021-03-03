import logging


#THIS IS THE PRACTISE for logger

logger = logging.getLogger(__name__)
#logging.fileHandler will help you to pass location
#logger will have knowledge on which file to pass info

fielHandler =logging.FileHandler("logging.log")
formatter =logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
fielHandler.setFormatter(formatter)
logger.addHandler(fielHandler)
#can I see just error logs? below will help you

logger.setLevel(logging.INFO)

logger.debug("A debug statement is executed")
logger.info("Information statement")
logger.error("")
logger.warning("Something is in warning mode")
logger.critical("Critical issue")

#SUMMARY: 1. Create a file name called test_loggingPractise.py
#2. import logging method
#3. create logger.debug, info,warning,error,critical methods
#4. create a file called logger.log using logging.Filehandler method n pass file name
#5. need to format file using using logging.formatter(pass time , level, name and message ) name this as formatter
#6. you need to set the format again using logging.setformat(pass in formatter)
#7.logger.addhandler (pass filehadler here)
#8 set level using logger.setLevel(logging.INFO)
logger = logging.getLogger(__name__) # this is to print the name of the test case logs


logger.debug("A debug statement is executed ")
logger.info("Information")
logger.warning("something is in warning mode")
logger.error("An error has occured")
logger.critical("Critical issue")

# now we need to pass all this log info into file
logger = logging.getLogger(__name__) # this is to print the name of the test case logs
fileHandler = logging.FileHandler("logging.log") # here we create n gave name to the file
# now we need to pass all logging info into file in a format. so we need to use a formatter method
formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)



logger.debug("A debug statement is executed ")
logger.info("Information")
logger.warning("something is in warning mode")
logger.error("An error has occured")
logger.critical("Critical issue")

#another way is not a good way
logging.basicConfig(filename="loginfile.log",
                    format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S:%p',
                    level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("A debug statement is executed ")
logger.info("Information")
logger.warning("something is in warning mode")
logger.error("An error has occured")
logger.critical("Critical issue")

