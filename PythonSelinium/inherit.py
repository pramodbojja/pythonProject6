from PythonSelinium.classDemo import Calculator


class child_inherit(Calculator):
    num2 = 250

    def __init__(self): # If there is any constructor in Calculator class, then
        Calculator.__init__(self,2,10) #you must use calculator.--init-- method and enter values


    def getComplete_data(self):
        return self.num2 + self.num +self.summation() # here you will get an erorr because in summation there is no value stored
        #in self.firstnumber and self.second number in calssDemo.py

obj = child_inherit()
print(obj.getComplete_data())
print(obj.num2)
print(obj.summation())
