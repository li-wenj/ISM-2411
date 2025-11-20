#collecting customer info
customer_name_raw = input("Enter customer name: ")
customer_email_raw = input("Enter customer email: ")

#collecting order info
product_name_raw = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

#applying string methods
customer_name = customer_name_raw.strip().title()
customer_email = customer_email_raw.strip().lower()
product_name = product_name_raw.strip().title()

#calculations
subtotal = quantity * unit_price
tax_amount = subtotal * 0.085
order_total = subtotal + tax_amount

#displaying order summary
print("\nORDER SUMMARY")
print("=" * 13)
print(f"Customer: {customer_name}")
print(f"Email: {customer_email}")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8.5%): ${tax_amount:.2f}")
print(f"Order Total: ${order_total:.2f}")