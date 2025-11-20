#Welcome message
print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

#Sample quarterly sales data 
#Format: [product_name, category, price, quantity_sold, employee_id]
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

#Employee information
#Format: {employee_id: [name, commission_rate]}
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

#create a function to calculate and return total sales revenue
def calculate_total_sales():
    """
    Calculates the total revenue from all sales.
    
    Returns:
        float: The total sales revenue.
    """
    total_sales_revenue = 0.0
    for sale in sales_data:
        price = sale[2]
        quantity = sale[3]
        total_sales_revenue += price * quantity
    return total_sales_revenue

#create a function to calculate the total sales for a specific category
def calculate_category_sales(category):
    """
    Calculates the total revenue from sales in a specific product category.
    
    Args:
        category (str): The product category to calculate sales for.
        
    Returns:
        float: The total sales revenue for the specified category.
    """
    product_sales_revenue = 0.0
    for sale in sales_data:
        if sale[1] == category:
            price = sale[2]
            quantity = sale[3]
            product_sales_revenue += price * quantity
    return product_sales_revenue

#create a function to find the best-selling product
def find_best_selling_product():
    """
    Finds the product with the highest total sales revenue.
    
    Returns:
         tuple: A tuple containing the name and total sales revenue of a product.
    """
    product_sales = {}
    for sale in sales_data:
        product = sale[0]
        price = sale[2]
        quantity = sale[3]
        revenue = price * quantity
        
        if product in product_sales:
            product_sales[product] += revenue
        else:
            product_sales[product] = revenue

    best_seller = ""
    max_revenue = 0

    for product in product_sales:
        revenue = product_sales[product]
        if revenue > max_revenue:
            max_revenue = revenue
            best_seller = product
            
    return (best_seller, max_revenue)


#Commission Calculation Function
def calculate_employee_commission(employee_id):
    """
    Calculates the commission earned by a specific employee.
    
    Args:
        employee_id (str): The unique identifier of the employee.
        
    Returns:
        float: The commission amount earned.
    """
    total_sales = 0.0
    commission_rate = employees[employee_id][1]
    for sale in sales_data:
        if sale[4] == employee_id:
            price = sale[2]
            quantity = sale[3]
            total_sales += price * quantity
            
    commission_earned = total_sales * commission_rate
    return commission_earned

#Create a function to calculate total commission for all employees
def calculate_total_commission():
    """
    Calculates the aggregate commission earned by all employees across all sales
    Returns:
        float: The total commission amount earned by the entire sales team.
    """
    total_commission = 0.0
    for employee_id in employees:
        commission_earned = calculate_employee_commission(employee_id)
        total_commission += commission_earned
    return total_commission



#create a function to generate a sales summary
def generate_sales_summary(include_categories=True):
    """
    Generates a formatted sales summary report.
    
    Args:
        include_categories (bool, optional): Whether to include category breakdown.
            Defaults to True.
        
    Returns:
        str: Formatted report string.
    """
    total_revenue = calculate_total_sales()
    best_seller, best_seller_revenue = find_best_selling_product()
    
    summary = ""
    summary += f"Total Quarterly Sales: ${total_revenue:,.2f}"
    summary += f"\nBest-Selling Product: {best_seller} - ${best_seller_revenue:,.2f}\n"
    
    if include_categories:
        summary += "\nSALES BY CATEGORY:\n"
        
        unique_categories = []
        for sale in sales_data:
            category = sale[1]
            if category not in unique_categories:
                unique_categories.append(category)
        
        for category in unique_categories:
            category_revenue = calculate_category_sales(category)
            summary += f"{category}: ${category_revenue:.2f}\n"
    
    return summary

#Create a function to generate an employee performance report
def generate_employee_report():
    """
    Generates a formatted performance report for all employees,
    including sales and earned commission.

    Returns:
        str: A formatted string containing each employee's performance report.
    """
    report = ""

    for employee_id in employees:
        name = employees[employee_id][0]

        # Calculate total sales for this employee
        total_sales = 0.0
        for sale in sales_data:
            if sale[4] == employee_id:
                price = sale[2]
                quantity = sale[3]
                total_sales += price * quantity

        commission_earned = calculate_employee_commission(employee_id)

        report += (
            f"\nEmployee: {name}"
            f"\n  Total Sales: ${total_sales:.2f}"
            f"\n  Commission Earned: ${commission_earned:.2f}"
        )

    return report



#Create a function to get all products in a specific category
def get_products_by_category(category):
    """
    Returns all products belonging to a specific category.
    
    Args:
        category (str): The product category to filter by.
        
    Returns:
        list: List of products in the specified category.
    """
    products_in_category = []

    for sale in sales_data:
        if sale[1] == category:  # sale[1] is the category field
            products_in_category.append(sale)

    return products_in_category


#Create a function to calculate the average sale price
def calculate_average_sale_price():
    """
    Calculates the average sale price across all transactions.

    Returns:
        float: The average sale price across all products sold.
    """
    total_revenue = 0.0
    total_quantity = 0

    for sale in sales_data:
        price = sale[2]
        quantity = sale[3]
        total_revenue += price * quantity
        total_quantity += quantity

    average_price = total_revenue / total_quantity
    return average_price

# Main program flow - function calls to demonstrate your system
def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)
    
    # Calculate and display total sales
    print("\nTOTAL QUARTERLY SALES:")
    total_sales = calculate_total_sales()
    print(f"${total_sales:,.2f}")
    
    # Display category sales
    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    for category in categories:
        category_sales = calculate_category_sales(category)
        print(f"{category}: ${category_sales:.2f}")
    
    # Display best-selling product
    print("\nBEST-SELLING PRODUCT:")
    best_product, best_revenue = find_best_selling_product()
    print(f"{best_product} - ${best_revenue:.2f}")
    
    
    # Display employee commissions
    print("\nEMPLOYEE COMMISSIONS:")
    for emp_id in employees: 
        emp_name = employees[emp_id][0]
        commission = calculate_employee_commission(emp_id)
        print(f"{emp_name}: ${commission:.2f}")
    
    # Generate and display sales summary report
    print("\nQUARTERLY SALES SUMMARY REPORT:")
    sales_summary = generate_sales_summary()
    print(sales_summary)
    
    # Generate and display employee performance report
    print("\nEMPLOYEE PERFORMANCE REPORT:")
    emp_report = generate_employee_report()
    print(emp_report)

# Run the main program
if __name__ == "__main__":
    main()