#Simple greeting
name = input('What is your name? ')
print(f'Welcome, {name}')

print('This program adds two numbers')
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
print(f'A + B = {A + B}')

EvenOrOdd = int(input('Enter a nuber to know if it is even or odd": '))
if EvenOrOdd%2 == 0:
    print(f'{EvenOrOdd} is an even number')
else:
    print(f'{EvenOrOdd} is an odd number')

C = int(input("What's the temperature today?"))
F = (C * 9/5) + 32
print(f"Your temperature in Farenheit is, {F}")

y = int(input('Enter a number: '))
if y > 0:
    print('This is a positive number')
elif y < 0:
    print('This is a negative number')
elif y == 0:
    print('Zero detected!!')
else:
    print('This is not a digit')