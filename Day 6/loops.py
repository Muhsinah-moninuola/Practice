#Iterating a sequence
"""
numbers = [34, 67, 89, 23, 45, 67]
indices = range(len(numbers))
for index in indices:
    print (f"index:{index}, number: {numbers[index]}")

#iterating through a dictionary
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)
#this will only give the key because the items do not have a positional index, however, associated value can be gotten 
#using the [] or the get()
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (f"{x} : {numbers[x]}")

#Understanding the forelse loop
for count in range(6):
    print(f"iteration no. {count}")
else:
    print("For loop is over, now in else block")
    print('end of loop')
"""

#nested loops
for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print ("{:3d}".format(k), end=' ')
   print()
