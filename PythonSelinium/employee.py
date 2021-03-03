import logging
logger = logging.getLogger(__name__) # here __name__ variable
fileHandler = logging.FileHandler('employee.log')
formatter =logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)





class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #before entering logger vaiable - logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        #after entering logger variable - logging.info ('Created Employee: {} - {}'.format(self.fullname, self.email))
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')


