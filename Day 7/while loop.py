"""
count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))

var = '0'
while var.isnumeric()==True:
   var=input('enter a number..')
   if var.isnumeric()==True:
      print ("Your input", var)
print ("End of while loop")

var = 1
while var == 1 : # This constructs an infinite loop
   num = int(input("Enter a number :"))
   print ("You entered: ", num)
print ("Good bye!")

while True:
    print("Still running...")
else:
    print("You’ll never see this.")

count = 1
while count <= 10:
    print("Count is:", count)
    
    if count == 5:
        print("Breaking the loop early!")
        break  # forcefully exits the loop here
    
    count += 1

#Alarm clock that stops at  particular time as set by the user
count = 10
stop_at = int(input('WHat time do you want the alarm to stop? '))
while count >=1:
    print(f'{count} time alarm!! wake upp!')

    if count == stop_at:
        print('This is your last chance, wake upp')
        break

    count -= 1
print(f"Alarm stopped at {count}! No more snoozing!")

#examples
print ('First example')
for letter in 'Python': # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)

print ('Second example')
var = 10 # Second Example
while var > 0:
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break
print ("Good bye!")

#to find a number in a list
no = int(input('Enter a number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
   if num==no:
      print ('number found in list')
      break
else:
   print ('number not found in list')

#to check for prime number
number = int(input('Enter a number to know if its a prime number or not: '))
check = range(2, number)
for num in check:
   if number%num == 0:
      print(f'{number} is not a prime number')
      break
else:
   print(f'{number} is a prime number')

for letter in 'Python': # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10 # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")


for num in range(2, 101):  # Start from 2, because 1 is not a prime number
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Optimization: check up to the square root of num
        if num % i == 0:
            is_prime = False
            break  # no need to check further
    if is_prime:
        print(num)

num = 60
print ("Prime factors for: ", num)
d=2
while num>1:
   if num%d==0:
      print (d)
      num=num/d
      continue
   d=d+1
"""

pet = "Cat"

match pet.lower():
    case "dog":
        print("Barks")
    case "cat":
        print("Meows")
    case _:
        print("Unknown pet")

