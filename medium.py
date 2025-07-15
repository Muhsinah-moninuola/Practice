count = 1
while True:
    print('Hi, what calculation would you like to perform today?' )
    operation = int(input('1: addidtion\n2: Subtraction\n3: Multiplication\n4: Division:\n'))
    A = int(input('Enter the first value: '))
    B = int(input('Enter the second value: '))
    if operation == 1:
        print(f'{A} + {B} = {A + B}')
    elif operation == 2:
        if A > B:
            print(f'{A} - {B} = {A - B}')
        else:
            print (f'{B} - {A} = {B - A}')
    elif operation == 3:
        print(f'{A} x {B} = {A * B}')
    elif operation == 4:
        print(f'{A}/{B} = {A/B}')
    else:
        print('kindly check the options again')
    choice = input("\nWould you like to perform another calculation? (yes/no): ")
    if choice.lower() != "yes":
            print("Goodbye! 👋")
            break