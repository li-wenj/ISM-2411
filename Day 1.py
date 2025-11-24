# My First Business Python Program
# This line is a comment - Python ignores it. It's just a note for humans.

# Use the print() function to display a message in the Shell
print("Welcome to Business Python!")

# Let's imagine we have revenue data from four different sales regions.
# We use 'variables' to store these numbers. Think of a variable like a labeled box.
# Here, 'north_revenue' is the label, and 50000 is the value inside the box.
north_revenue = 50000
south_revenue = 40000
east_revenue = 45000
west_revenue = 55000

# Now, let's calculate the total revenue.
# We create another variable called 'total_revenue'.
# Its value will be the sum of the values stored in the other revenue variables.
# The '=' sign here means 'assign the result of the calculation on the right
# to the variable on the left'. It's not the same as mathematical equality.
total_revenue = north_revenue + south_revenue + east_revenue + west_revenue

# Finally, let's display the calculated total revenue.
# We use the print() function again. We can give it multiple things to print,
# separated by commas. Python will automatically put a space between them.
print("Total Revenue: $", total_revenue)

# End of the program.