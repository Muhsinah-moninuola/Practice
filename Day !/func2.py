x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

w = 50

def myfunc9():
    print("You are "  +  str (w) +  " Years old")

myfunc9()

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))