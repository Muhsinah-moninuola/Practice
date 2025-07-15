"""
Food = input("What would you like to eat today? ").strip().lower()

match Food:
    case ("indomie"):
        print("Indomie is a great choice! Quick to make and delicious. However, it is not very nutritous")
    case ("rice"):
        print("Rice is a good source of carbohydrate, Great choice!")
    case ("bread"):
        print("Bread is a great choice")
    case("beans"):
        print("Nice! Get your proteins and grow very well")
    case _:
        print("Option  not available")


TrafficLight = input("What color is dsiplayed on the traffic light? ").strip().lower()

match TrafficLight:
    case "red":
        print("Stop")
    case "yellow":
        print ("Ready")
    case "green":
        print("Go")
    case _:
        print("Dont move")



def check_grade(mygrade):
    match mygrade.strip().lower():
        case "a":
            print(f"Your grade, {mygrade.upper()} is an Excellent grade")
        case "b":
            print(f'Your grade, {mygrade.upper()}, is very Good')
        case "c":
            print(f"Your grade, {mygrade.upper() } is a good grade") 
        case "d" :
            print(f"Your grade is {mygrade.upper()  } is poor but you can do better")
        case "f":
            print(f"Your grade is {mygrade.upper() }, You have failed")

grade = input("Kindly input your grade to know your category ")
check_grade(grade)


def guess_type(value):
    match value:
        case _ if value.isdigit():
            print("You entered a number.")
        case _ if value.lower() in ["yes", "no"]:
            print("You entered a boolean-like word.")
        case _:
            print("You entered a string or something else.")
user_input = input("Enter something: ").strip()
guess_type(user_input)
"""

print ("Welcome to Muhsinah's' internet banking")
print("Enter A if you want to check balance")
print("Enter B if you want yo Deposit")
print("Enter C if you want to withdraw")
print("Enter D if you want to exit")


def account_operation(user):
    match UserInput.strip().upper():
        case 'A':
            print(f"Dear {Username}, Your balance is 10,000, thank you for using our services")
        case "B":
            print(f'Dear {Username}, Deposit Functionality coming soon')
        case 'C':
            print(f'Dear {Username}, Withdraw functionality coming soon')
        case 'D':
            print(f'Dear {Username}, thank you for banking with us')
        case _:
            print("Error! kindly check the options well")
       
Username = input("What is your name: ").strip()
UserInput = input("What do you want to do? Kindly input the correct option ")
account_operation(UserInput)
