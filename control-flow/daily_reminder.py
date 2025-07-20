# daily_reminder.py

# Ask for the task
task = input("Enter your task: ")

# Ask for priority
priority = input("Priority (high/medium/low): ").lower().strip()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Match based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority"

# Add info about time-sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += " that you can complete when you have time."

# Final output
print()
print(message)

