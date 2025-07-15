Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print ('Examplr of a startup file')
Examplr of a startup file
pythonapp
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pythonapp
NameError: name 'pythonapp' is not defined
-m venv myvenv
SyntaxError: invalid syntax
help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
import keyword
keyword.iskeyowrd('else')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    keyword.iskeyowrd('else')
AttributeError: module 'keyword' has no attribute 'iskeyowrd'. Did you mean: 'iskeyword'?
import keyword
keyword.iskeyword('else')
True
keyword.iskeyword('Hello')
False
'May'
'May'
id('May')
2458744822672
18
18
id('18')
2458705602928
width = 10
height = 15
area = width*hight
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    area = width*hight
NameError: name 'hight' is not defined. Did you mean: 'height'?
area=width*height
width = wo
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    width = wo
NameError: name 'wo' is not defined
width=10
height=20
area=width*height
area
200
perimeter=2*(width+height)
perimeter
60
print ('Area =', area)
Area = 200
x=5
y=10
x+y=z
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a=b=10
a is b
True
id(a), id(b)
(140731613267144, 140731613267144)
sqrt-1
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sqrt-1
NameError: name 'sqrt' is not defined
import math
sqrt -1
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sqrt -1
NameError: name 'sqrt' is not defined
'welcome to "python tutorial" from tutorial point'
'welcome to "python tutorial" from tutorial point'
[2023, 'python', 3.11, 5+6j, 1.2E-4]
[2023, 'python', 3.11, (5+6j), 0.00012]
type([2023, 'python', 3.11, 5+6j, 1.2E-4])
<class 'list'>
2023, "Python", 3.11, 5+6j, 1.23E-4
(2023, 'Python', 3.11, (5+6j), 0.000123)
F1=(1,2,3,4)
T1=[1,2,3,4]
T1[1]
2
F1[1]
2
F1[1]=50
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    F1[1]=50
TypeError: 'tuple' object does not support item assignment
T1[1]=25
t1
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t1
NameError: name 't1' is not defined. Did you mean: 'T1'?
T1
[1, 25, 3, 4]
{2023, "Python", 3.11, 5+6j, 1.23E-4}
{(5+6j), 3.11, 0.000123, 2023, 'Python'}
{['One', 'Two', 'Three'], 1,2,3, (1.0, 2.0, 3.0)}
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    {['One', 'Two', 'Three'], 1,2,3, (1.0, 2.0, 3.0)}
TypeError: unhashable type: 'list'
a=True
b=10.5
c=a+b
print(c)
11.5
a=int(water)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a=int(water)
NameError: name 'water' is not defined. Did you mean: 'iter'?
a=int('water')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a=int('water')
ValueError: invalid literal for int() with base 10: 'water'
a=int(True)
a
1
a=int(10.5)
a=int(10.5)
a=int('10.5')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a=int('10.5')
ValueError: invalid literal for int() with base 10: '10.5'
a=int(6.5)
print (a)
6
a=int(10.9)
print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(a)
10
a=int("110001",2)
a
49
var =3/4
print (var)
0.75
>>> var = "3/4"
>>> print (var)
3/4
>>> var ="\u00BE"
>>> print(var)
¾
>>> string = "\u20B9)"
>>> print(string)
₹)
>>> tobytes = string.encode('utf-8')
>>> print(tobytes)
b'\xe2\x82\xb9)'
>>> string = tobytes.decode('utf-8')
>>> print(string)
₹)
>>> #using octal notation
>>> x =0034
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> x=0o34
>>> print("0o34 in octal is," x, type(x))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("0o34 in octal is,", x, type(x))
0o34 in octal is, 28 <class 'int'>
>>> y = 1.23E5
>>> print ("1.23e5 in scientific notation is,",x type(x))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print ("1.23e5 in scientific notation is,",x, type(x))
1.23e5 in scientific notation is, 28 <class 'int'>
>>> print ("1.23e5 in scientific notation is,",y, type(y))
1.23e5 in scientific notation is, 123000.0 <class 'float'>
>>> a=7.5+7.5j
>>> b=2.5
>>> print("Division of complex and float")
Division of complex and float
>>> print(a/b)
(3+3j)
>>> print(b/a)
(0.16666666666666666-0.16666666666666666j)
