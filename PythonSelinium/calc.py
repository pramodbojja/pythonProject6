import inspect
import logging
import employee
 # since we already imported employee module root will go into employee.log file n run, but it will run all of calc functions in
 #employee.log file
# 5 levesl
#Debug
#info
#debug
#error
#critilcal error

#logging.basicConfig(filename="calc.log",
                    #format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                    #datefmt='%m/%d/%y %I:%M:%S:%p',
                   # level=logging.DEBUG)
#2021-02-02 19:19:41,307: INFO: __main__: Created Employee: Jane Doe - Jane.Doe@email.com
#on regarding INFO: __main__: Created Employee: which means we are running directly from employee file
# 2021-02-02 19:24:01,981: INFO: __main__: Created Employee: John Smith - John.Smith@email.com#above line explanati

logger_name = inspect.stack()[1][3] #need to know more about it
logger = logging.getLogger(logger_name)
fileHandler = logging.FileHandler("calc.log")
fileHandler.setLevel(logging.ERROR) # this step will only report errors
formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler )#here we can add all debug/error/info to file handler

stream_handler = logging.StreamHandler() #here we can also add stream handler, that can only disply those
# errors to the console
logger.addHandler(stream_handler)

def add(x,y):
  return x+y


def sub(x,y):
  return x-y


def div(x,y):
  try:
    result = x/y
  except ZeroDivisionError:
    logger.error("tried to divided by zero")
  else:
    return result


def mult(x,y):
  return x*y

num1 = 5
num2 = 0

sub_result = sub(num1,num2)
logger.debug('sub:{} - {}= {}'.format(num1,num2,sub_result))

div_result = div(num1,num2)
logger.debug('div:{} / {} = {}'.format(num1,num2,div_result))

add_result = add(num1,num2)
logger.debug('add:{} + {}= {}'.format(num1,num2,add_result))

mult_result = mult(num1,num2)
logger.debug('mult:{} * {} = {}'.format(num1,num2,mult_result))
