def reminder_app(task_data):
    reminders = {}  # stores reminders separately from task_data
    
    print("reminder setup:\n")

    if not task_data: #if task data is an empty dictionary
        print('You have no tasks to set reinders for.\n')
        return #exist function if no tasks exist
    
    print("Here are your current tasks:")
    for time, task in task_data.items():
        print(f"{time} : {task}")

    while True:
        set_time = input("\n Enter the time of the task you want to set a reminder, kindly enter 'exit' if you want to quit ").strip()

        if set_time.lower() == 'exit':
            break
        
        if set_time in task_data:
            reminders[set_time] = task_data[set_time]
            print(f" Reminder set for '{task_data[set_time]}' at {set_time}!")
        else:
            print("No task found at that time. Try again.")
      
            break
    

task_manager = {} #Creates an empty dictionary

print('Welcome to your task manager!') #simple greeting

#Starts a loop till the user decides to quit
while True:
    print('\nWhat would you like to do? Kindly check the options carefully')
    print('1: Add new task')
    print('2: Delete a task')
    print('3: View tasks')
    print('4: Set reminder instead')
    print('5: Exit')

    choice = int(input('Choose an option among the ones provided ')) #Asks the user to pick an options and will be used to run specific block of code

    if choice == 1:
        task = input('Add a new task here: ')
        time = input(f'What time would you perform "{task}"? ')
        task_manager[time] = task #adds the new task to the dictionary with the time being the key
        print(f'You have added Task "{task}" at "{time}"')
    
    elif choice == 2:
        time = input('Enter the time of the task you want to remove: ')
        if time in task_manager:
            removed_task = task_manager.pop(time) #removed the task at the specified time
            print(f"Removed task: '{removed_task}' at {time}")
        else:
            print('No task at that time')
    
    elif choice == 3:
        if not task_manager:
            print('You have no task scheduled for today')
        else:
            print('\nHere are your tasks for the day')
            for time, task in task_manager.items(): #loops through the tasks to give the output one after the other
                print(f'{time} : {task}')
    elif choice == 4:
        reminder_app(task_manager)
    
    elif choice == 5:
        print('Goodbye')
        break

    else:
        print('Kindly check the options and choose between 1,2,3, or 4.')


