#this program is a simple grading system that adds students and gives them a grade based on their score

def grade(score): #this is a function to classify scores into grade
    if score in range(90,101):
        return 'A'
    elif score in range(80, 90):
        return 'B'
    elif score in range(70,80):
        return 'C'
    elif score in range(60,70):
        return 'D'
    elif score <= 60:
        return 'F'
    else:
        return 'kindly enter a valid score'
    
    

student_record ={} #dictionary to store students record
while True:
    print('\n1: Add new student')
    print('2: View all students and thier grades')
    print('3: Delete a student and thier record')
    print('4: Exit')

    try:
        choice = int(input('What would you like to do? '))
    except ValueError:
        print('This is not a valid option, check again')
        continue
    

    if choice == 1:
        name = input("\nEnter the student's name: ")
        try:
            score = int(input("Enter the corresponding score: "))
        except ValueError:
            print('Invalid number, enter a valid number')
            continue
        student_record[name] = score
        print(f'Student "{name}" with grade "{grade (score)}" added!')

    elif choice == 2:
        if not student_record:
            print('No student on the system yet, kindly enter a student to view the records')
        else:
            print('\nThese are the students on record currently: ')
            for name,score in student_record.items():
                print(f'{name} : {score} 👉 {grade(score)}')
    
    elif choice == 3:
        print('\nThese are the students on record currently: ')
        for name in student_record.items():
            print(f'{name}')
        delete = input('Enter the name you want to erase from the system: ')
        if delete not in student_record:
            print('Student not in record')
        else:
            del student_record[delete]
            print(f"Student '{delete}' deleted.")
    
    elif choice == 4:
        ('Thank you for using this app!')
        break

    else:
        print('Kindly choose between options 1-4')
    


