#welcome message and user input
print("Welcome to my python program!")
hours = input("How many hours did you practice today?")

#data conversion and calculation
hours = float(hours)
weekly_hours = hours * 7

#display results
print(f"You are on track to practice {weekly_hours} this week")

#error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()