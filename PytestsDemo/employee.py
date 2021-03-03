class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    @fullname.setter
    def fullname(self,name):
        first,last = name.split("")
        self.first= first
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @classmethod
    def set_raiseamount(cls,amount):
        cls.raise_amt = amount

#Employee.set_raiseamount(1.5)
emp_1 = Employee("raju","Kaka",85260)
emp_2 = Employee("ramu","Kaka",98526)
emp_3= Employee("malli","Kaka",44520)

emp_1.last= "raka"

print(emp_1.pay)
print(emp_3.fullname)
print(emp_1.fullname)
print(emp_1.email)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
emp_2.apply_raise()
print(emp_2.pay)