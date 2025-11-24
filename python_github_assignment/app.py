print("Welcome to my python program!")
hours = input("How many hours did you practice today?")
hours = float(hours)
weekly_hours = hours * 7
print(f"You are on track to practice {weekly_hours} this week")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()