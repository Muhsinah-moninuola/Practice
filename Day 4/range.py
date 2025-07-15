numbers = range(5)
print (list(numbers))
'''
start is 0 by default,
step is 1 by default,
range generated from 0 to 4
'''
num = range(10,20) #starts from 10 then prints with the default 1 increment
print(list(num))

#syntax for range with specified difference; range(first value, second value, the step/diiffernce) 
nums = range(10,20,2)
print (list(nums))

#for loop with range without listing it
for num in range(5):
 print (num, end=' ')
print()
for num in range(10,20):
 print (num, end=' ')
print()
for num in range(1, 10, 2):
 print (num, end=' ')

#to get the factorial of a number

fact = 1
N = 5
for x in range(1,N+1):
 fact = fact*x

print(f'The factorial of {N} is {fact}')
print('The factorial of {} is {}'. format(N, fact))

 
 