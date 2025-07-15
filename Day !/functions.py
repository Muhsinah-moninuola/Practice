def greet():
    print("Hello!")

greet() #global function call

y = 10  #GLOBAL VARIABLE

def show():
    print (y)  #Can access x even inside the function

show()
print(y)  #Can also access x here

x = "awesome"

def myfunc():
    x = "fantastic" #this is a local variable
    print("Python is " + x)

myfunc()

print("Python is " + x)