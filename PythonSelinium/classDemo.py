#now we need to understand constuctor.
#The constructor is a method that is called when an object is created.
# constructor name should always be __init__
# calss varible = whatever variable you will define inside your class is called variable
#example is Num = 100 above
#instance varible  = these will be created inside constructor or __init__ method, these will change when you create
#new object unlike class variables
# slef is a gloable varibale can be used for calss varable like self. calss variable

class Calculator:
    num = 100

    def __init__(self,a,b):# this is the constructor, self is object
        self.firstnumber = a  #these are the instance varibales & firstnumber and secondnumber are values
        self.secondnumber = b
        print("Constructor will be called automatically when created object")

    def get_data(self):
        print("I am now executing method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num #(here u can use class.class varable or self.class variable)

#math =Calculator() # now call this as object, any name
math = Calculator(2,3) # when you add a, b . you must add a, b in your __init__ method
math.get_data() # you can call method
print(math.summation())# or you can call variable, Note: there is no parenthesis for calling variabl ()

obj = Calculator(4,5)
print(obj.summation())


