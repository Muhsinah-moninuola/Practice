"""
def greetings():
   "This is docstring of greetings function"
   print ("Hello World")
   return
greetings()

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;
# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def testfunction(arg):
   print ("ID inside the function:", id(arg))
var="Hello"
print ("ID before passing:", id(var))
testfunction(var)

def add(x,y):
   z=x+y
   return z

a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))

#this is a default function
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return
# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="sola" )
"""

#Example 2 on default functions
def percent(phy, maths, maxmarks=200):
   val = (phy+maths)*100/maxmarks
   
   return val

phy = 70
maths = 80
result = percent(phy, maths)
print(f"Your percentage is; {result: .2f}%")
result = percent(phy = 90, maths = 80)
print(f"Your percentage is; {result: .2f}%")

def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(10,5)
division(5,10)
division(den = 14, num = 7)
division(14, den = 7)

def f(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

f(1, 2, 3, x=10, y=20)
# Positional: (1, 2, 3)
# Keyword: {'x': 10, 'y': 20}

