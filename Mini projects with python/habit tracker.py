habit_data = {}  # key = habit name, value = number of days completed

print("Welcome to your Habit Tracker!")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a new habit")
    print("2. Mark habit as done today")
    print("3. View all habits and progress")
    print("4. Delete a habit")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        habit = input("\nEnter the habit you want to track: ").strip().lower()
        if habit in habit_data:
            print(f"You're already tracking '{habit}'")
        else:
            habit_data[habit.lower()] = 0
            print(f"Habit '{habit}' added!")

    elif choice == '2':
        habit = input("Which habit did you complete today? ").strip()
        if habit in habit_data:
            habit_data[habit.lower()] += 1
            print(f"Great! You've completed '{habit}' for {habit_data[habit]} day(s).")
        else:
            print(f"'{habit}' is not in your habit list.")

    elif choice == '3':
        if not habit_data:
            print("You’re not tracking any habits yet.")
        else:
            print("\nYour Habits Progress:")
            for habit, count in habit_data.items():
                print(f"{habit}: {count} day(s)")

    elif choice == '4':
        habit = input("Enter the habit to remove: ").strip()
        if habit in habit_data:
            habit_data.pop(habit)
            print(f"Habit '{habit}' removed.")
        else:
            print("That habit doesn't exist.")

    elif choice == '5':
        print("Goodbye! Keep building good habits!")
        break

    else:
        print("Invalid choice. Please pick between 1 and 5.")
