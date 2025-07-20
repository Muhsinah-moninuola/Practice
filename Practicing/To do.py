Todo = []
Time = []
print('Welcome, what would you like to do for today?')

#Ask the number of tasks the user wants to add
num_tasks = int(input('How many tasks do you want to add? '))

#loop to collect each task ansd time
for i in range (num_tasks):
    task = input(f'Enter task #{i+1} ')
    todo_time = input(f'What time will you do "{task}" ')
    Todo.append(task)
    Time.append (todo_time)
print('These are your activities for today')
for i in range(len(Todo)):
    print(f"{Time[i]} : {Todo[i]}")

    
