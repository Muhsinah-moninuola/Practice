#Registration phase
UserName = input('enter your User Name ')
Course = input('Enter your course ')
Age = input ('How old are you? ')
Password = input('Create a password ')

#Store details
stored_username = UserName.strip().lower()
stored_password = Password.strip()

#Login Phase
print('\n Now Please login\n')
login_name = input('Enter your Username: ').strip().lower()
login_password = input('Enter your password: ').strip()

#login function
def login(user_name, password):
    global stored_password
    #Checks if the username is correct
    if user_name == stored_username:
        print('Username Correct')
    
        retry = 0
        while retry < 3:
            if password == stored_password: #Checks if the password is correct
                print ('Login Successful')
                print('These are the details on your profile')
                print(f'Username:{UserName}\nCourse: {Course}\nAge:{Age}')
                return #End the function after successful login
            else:
                print('Password Incorrect')
                retry += 1
                if retry < 3:
                    password = input('Try again. Enter password: ').strip()
        
        print('Too many failed attempts. Can’t remember your password? Use "Forgot Password?"')
        #Restting the password
        reset = input('Do you wanrt to reset your password? Yes or No?: ').strip().lower() #setting a new password
        if reset == 'yes':
            print("You can set your new password, kindly take note")
            new_password = input('enter a new password: ').strip()
            stored_password = new_password
            #login again
            print('Password reset successful. Please login again\n')
            password = input('Enter your new password: ')
            if password == stored_password:
                print('Finally logged in!')
                print(f'Username: {UserName}\nCourse: {Course}\nAge: {Age}')
            else:
                print('Still incorrect. Please try again later.')
        else:
            print('Login cancelled.')

    else:
        print('Invalid login credentials')

login(login_name, login_password)