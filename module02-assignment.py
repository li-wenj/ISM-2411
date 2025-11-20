#Defining variables
product_name = "golf clubs"
units_sold_str = "10"
price_per_unit_str = "2499.99"
tax_rate = 0.38
discount_rate = 0.15

#Converting variable data types
units_sold = int(units_sold_str)
price_per_unit= float(price_per_unit_str)

taxed_price = price_per_unit * (1 + tax_rate) #Calculating price after tax
net_price = taxed_price * (1 - discount_rate) #Calculating price after tax and discount
total_revenue = net_price * units_sold #Calculating total revenue by multiplying net price by units sold

#Displaying summary using f-strings
print(f"Product: {product_name}")
print(f"Net Price: ${net_price:.2f}")
print(f"Total Revenue: ${total_revenue:.2f}")