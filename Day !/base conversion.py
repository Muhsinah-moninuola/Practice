#This app helps to convert from one base to the other
print("Welcome to the Base Converter!")
print("You can convert:")
print("1. From base 10 to binary, octal, or hexadecimal")
print("2. From binary, octal, or hexadecimal to base 10")

choice = input("Choose option (1 or 2): "). strip()
if choice == 1: # converts from base 10 to other bases

    try:
        original_num = int(input("What number do you want to convert? "))
        baseConvert = (input("What base do you want to convert to? Binary, Octal(base 8), Hexadecimal(base 16) ")).strip().lower()
        if baseConvert == "binary":
            ansB = bin(original_num)
            print(f"Your number in base 2 is {ansB[2:]},")
        elif baseConvert == "octal":
            ansO = oct(original_num)
            print(f"Your number in base 8, is {ansO[2:]}")
        elif baseConvert =="hexadecimal":
            ansH = hex(original_num)
            print(f"Your number in base 16, is {ansH[2:].upper()}")
        else:
            print ("Not available to convert")
    except ValueError:
        print("Invalid base 10 number.")

elif choice == "2":
    #this converts from other bases to base 10
    num = input("enter the number you want to convert: ")
    baseFrom = input("What base is the value; Binary, Octal(base 8), Hexadecimal(base 16) ").strip().lower()
    
    try:
    
        if baseFrom == "binary":
            result = int(num, 2)
        elif baseFrom == "octal":
            result = int(num, 8)
        elif baseFrom == "hexadecimal":
            result = int(num, 16)
        else:
            print (" Invaliid base")
            result = None
        if result is not None:
            print(f"Your value in base 10 is {result}")
    except ValueError:
        print("Invalid number for the selected base.")
else:
    print("Invalid option. Please choose 1 or 2.")



