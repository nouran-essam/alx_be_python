# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ").lower().strip()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Match case to handle priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority"

# Modify message if the task is time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "low" in message:
        message += ". Consider completing it when you have free time."
    else:
        message += " but can be scheduled during the day."

# Print the final reminder
print()
print(message)
