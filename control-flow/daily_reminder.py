# daily_reminder.py

# Ask for the task description
task = input("Enter your task: ")

# Ask for the priority
priority = input("Priority (high/medium/low): ").lower().strip()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Use match case to determine the base reminder message
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that you can complete during the day.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task that you can complete when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task that you can complete when you have free time.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority. Please review it manually.")

