#QuickMart Sales Analysis
#Welcome message
print("=" * 60)
print("QUICKMART SALES ANALYSIS")
print("=" * 60)

#Monthly sales data per store (in thousands of dollars)
#Data structure: Dictionary with store locations as keys
#Each store contains a list of 12 monthly sales figures (Jan-Dec)
sales_data = {
    "Downtown": [120.5, 115.8, 131.2, 140.5, 150.2, 160.1, 155.3, 148.9, 152.5, 160.8, 165.2, 180.3],
    "Suburb Mall": [85.6, 90.2, 93.5, 100.8, 110.5, 115.7, 120.2, 118.5, 125.6, 130.2, 140.8, 155.5],
    "Westside": [95.2, 88.7, 92.3, 100.5, 105.8, 110.2, 115.7, 120.5, 125.8, 130.2, 135.5, 145.8],
    "University": [55.3, 60.2, 65.8, 70.5, 65.2, 50.1, 45.2, 55.8, 80.5, 85.9, 90.2, 95.3]
}

#Store locations and month names
locations = list(sales_data.keys())
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

#Calculate the total sales for each month across all stores
#Initialize a list to store the total monthly sales
monthly_totals = []
for month_index in range(12):
    total = 0
    for store in locations:
        total += sales_data[store][month_index]
    monthly_totals.append(total)

#Find the month with the highest and lowest total sales
#Initialize variables to track highest and lowest sales
highest_month_index = 0
lowest_month_index = 0
highest_sales = float(0)
lowest_sales = float('inf')  #Start with infinity for comparison
for month_index in range(len(monthly_totals)):
    if monthly_totals[month_index] > highest_sales:
        highest_sales = monthly_totals[month_index]
        highest_month_index = month_index
    if monthly_totals[month_index] < lowest_sales:
        lowest_sales = monthly_totals[month_index]
        lowest_month_index = month_index
    
#Calculate the average monthly sales across all stores
total_monthly_sales = 0
for sales in monthly_totals:
    total_monthly_sales += sales
average_monthly_sales = float(total_monthly_sales / 12)

#Find the store with the highest annual sales
#Initialize variables to track the best performing store
best_store = ""
best_store_sales = 0
for store in sales_data:
    total_annual_sales_store = sum(sales_data[store])
    if total_annual_sales_store > best_store_sales:
        best_store_sales = total_annual_sales_store
        best_store = store


#Generate a monthly performance report using a while loop
performance_report = []
month_index = 0
while month_index < 12:
    month_sales = monthly_totals[month_index]
    if month_sales > average_monthly_sales:
        performance_indicator = "Above Average"
    elif month_sales < average_monthly_sales:
        performance_indicator = "Below Average"
    else:
        performance_indicator = "Average"
    message = f"Month: {months[month_index]}, Monthly Sales: ${month_sales:.2f}, Performance Indicator: {performance_indicator}"
    performance_report.append(message)
    month_index += 1

#Bonus challenge - Identify consecutive months with increasing sales
longest_growth_streak = 0
growth_streak_start = 0
current_streak = 0
current_start = 0
for month_index in range(1, len(monthly_totals)):
    if monthly_totals[month_index] > monthly_totals[month_index - 1]:
        # Sales increased compared to previous month
        if current_streak == 0:
            current_start = month_index - 1  # start of new streak
        current_streak += 1
    else:
        # Streak ended
        if current_streak > longest_growth_streak:
            longest_growth_streak = current_streak
            growth_streak_start = current_start
        current_streak = 0  # reset streak
# Check at the end in case the longest streak is at the end
if current_streak > longest_growth_streak:
    longest_growth_streak = current_streak
    growth_streak_start = current_start

#Print final summary
print("\n" + "=" * 60)
print("QUICKMART SALES ANALYSIS SUMMARY")
print("=" * 60)
print(f"Best Month: {months[highest_month_index]} - ${highest_sales:.2f}")
print(f"Worst Month: {months[lowest_month_index]} - ${lowest_sales:.2f}")
print(f"Average Monthly Sales: ${average_monthly_sales:.2f}")
print(f"Best Performing Store: {best_store} - ${best_store_sales:.2f}")
print(f"Longest Growth Streak: {longest_growth_streak} months starting in {months[growth_streak_start]}")
