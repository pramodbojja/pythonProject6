import logging

import logging

def test_logers():
    logger = logging.getLogger(__name__)
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
    return logger