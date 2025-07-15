"""
user = input('Who is trying to log in to the system? ').strip().lower()

match user:
    case "admin":
        print ("full access")
    case "manager":
        print ('full access')
    case "guest":
        print ("limited access")
    case _:
        print ('no access')
"""

def acess(user):
    user = userInput.strip().lower()
    match user:
        case "admin":
            return 'full acesss'
        case "manager":
            return 'full access'
        case "guest":
            return "limited access"
        case _:
            return 'no access'
        
userInput = input('wo is trying to access the website? ')
print(acess(userInput))
