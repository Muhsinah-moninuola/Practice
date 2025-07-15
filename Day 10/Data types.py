import random

print(random.randrange(1, 10))

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])

a = " Hello, World! "
print(a.strip()) 

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, I am " + str(age)
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print (txt)

print(bool("Hello"))
print(bool(15))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#to change an item values on the list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#to change a range of item values in the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#removes only the first instance of banana coz it appears twice 
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#the pop() method removes the last item because the index was not specified.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)