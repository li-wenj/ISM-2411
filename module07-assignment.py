# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

#Creating product tuples
product1 = ("P01", "iPhone 17", 800.00, 10, "Mobile Phones")
product2 = ("P02", "Samsung Z Fold", 1000.00, 7, "Mobile Phones")
product3 = ("P03", "Sony XM4", 500.00, 20, "Audio")
product4 = ("P04", "MacBook", 1200.00, 10, "Laptops")
product5 = ("P05", "Airpods Pro", 300.00, 25, "Audio")

#Create an inventory list containing all product tuples
inventory = [product1, product2, product3, product4, product5]

# Display all products
print("\nCurrent Inventory:")
print("-" * 60)
for product in inventory:
    print(product)

# Access specific elements
print("\n\nAccessing Specific Products:")
print("-" * 60)

first_product = inventory[0]
print(f"First product: {first_product}")
last_product = inventory[-1]
print(f"Last product: {last_product}")
third_product_name = inventory[2][1]
print(f"Third product name: {third_product_name}")
second_price = inventory[1][2]
second_quantity = inventory[1][3]
print(f"Second product price: {second_price}, second product quantity: {second_quantity}")



#Use slicing to get subsets
print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)

first_three = inventory[0:3]
print(f"First three products: {first_three}")
middle_products = inventory[2:5]
print(f"Products from index 2 to 4: {middle_products}")
all_except_first = inventory[1:]
print(f"All products except first: {all_except_first}")


# Add new products to inventory
print("\n\nAdding New Products:")
print("-" * 60)
product6 = ("P06", "Google Pixel", 700.00, 10, "Mobile Phones")
product7 = ("P07", "Airpods Max", 900.00, 15, "Audio")
inventory.append(product6)
inventory.append(product7)


#Remove a product
print("\n\nRemoving a Product:")
print("-" * 60)

removed_product = inventory.pop(2)
print("\nUpdated Inventory:")
for product in inventory:
    print(product)


# Insert a product at a specific position
print("\n\nInserting a Product:")
print("-" * 60)

product8 = ("P08", "Chromebook", 500.00, 10, "Laptops")
inventory.insert(1, product8)



# REDO TODO 4 and 5
print("\n\nAccessing Specific Products:")
print("-" * 60)

first_product = inventory[0]
print(f"First product: {first_product}")
last_product = inventory[-1]
print(f"Last product: {last_product}")
third_product_name = inventory[2][1]
print(f"Third product name: {third_product_name}")
second_price = inventory[1][2]
second_quantity = inventory[1][3]
print(f"Second product price: {second_price}, second product quantity: {second_quantity}")


print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)

first_three = inventory[0:3]
print(f"First three products: {first_three}")
middle_products = inventory[2:5]
print(f"Products from index 2 to 4: {middle_products}")
all_except_first = inventory[1:]
print(f"All products except first: {all_except_first}")

# Create category lists
# Go through your inventory and add products to appropriate category lists
print("\n\nProducts by Category:")
print("-" * 60)
mobile_phones = []
laptops = []
audio = []
for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_phones.append(product)
    elif product[4] == "Laptops":
        laptops.append(product)
    else:
        audio.append(product)

# Calculate inventory statistics
print("\n\nInventory Statistics:")
print("-" * 60)

total_products = len(inventory)
total_value = 0
product_names = []
product_prices = []
for product in inventory:
    price = product[2]
    quantity = product[3]
    total_value += price * quantity
    name = product[1]
    product_names.append(name)
    product_prices.append(price)

print(f"Total number of products: {total_products}")
print(f"Total inventory value: ${total_value}")
print(f"Product names: {product_names}")
print(f"Product prices: {product_prices}")


# Find expensive products using list comprehension
# Use a list comprehension to create a list of products that cost more than $500
# Hint: expensive_products = [product for product in inventory if product[2] > 500]
print("\n\nExpensive Products (> $500):")
print("-" * 60)

expensive_products = [product for product in inventory if product[2] > 500]
print(expensive_products)


# Low stock alert using list comprehension
# Use a list comprehension to create a list of products with quantity less than 5
# Hint: low_stock = [product for product in inventory if product[3] < 5]

print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)

low_stock = [product for product in inventory if product[3] < 5]
print(low_stock)


# Use a list comprehension to create a list of all product prices (store in original_prices)
# Then use another comprehension to apply a 10% discount to all prices (store in discounted_prices)
# Display both the original and discounted price lists
print("\n\nPrice Lists:")
print("-" * 60)

original_prices = [product[2] for product in inventory]
discounted_prices = [price * 0.9 for price in original_prices]
print(f"Original prices: {original_prices}")
print(f"Discounted prices: {discounted_prices}")

# Use a list comprehension to create a list of all product names in uppercase (store in uppercase_names)
# Then create another list with product codes (first 3 chars of ID + first 3 chars of name) (store in product_codes)
# Display both lists
print("\n\nFormatted Product Names:")
print("-" * 60)

uppercase_names = [product[1].upper() for product in inventory]
product_codes = [product[0][:3] + product[1][:3] for product in inventory]
print(f"Uppercase names: {uppercase_names}")
print(f"Product codes: {product_codes}")


# Use a for loop to:
# - Count how many products are in the "Mobile Phones" category (store in mobile_count)
# - Calculate the total value of all "Laptops" in stock (store in laptop_value)
# - Find the most expensive product in the inventory (store in most_expensive)
print("\n\nLoop-Based Analysis:")
print("-" * 60)

mobile_count = 0
laptop_value = 0
most_expensive = inventory[0]
for product in inventory:
    category = product[4]
    price = product[2]
    quantity = product[3]
    if category == "Mobile Phones":
        mobile_count += 1
    if category == "Laptops":
        laptop_value += price * quantity
    if price > most_expensive[2]:
        most_expensive = product


# Use loops and conditionals to:
# - Create a list of products that need restocking (quantity < 5) (store in restock_list)
# - Create a list of high-value items (price > $500 AND quantity > 10) (store in high_value_items)
# - Count products in different price ranges: under $100, $100-$500, over $500 (store counts in price_ranges dictionary)
print("\n\nConditional Analysis:")
print("-" * 60)

restock_list = []
high_value_items = []
price_ranges = {"under_100": 0, "100_to_500": 0, "over_500": 0}

for product in inventory:
    price = product[2]
    quantity = product[3]

    if quantity < 5:
        restock_list.append(product)
    if price > 500 and quantity > 10:
        high_value_items.append(product)
    if price < 100:
        price_ranges["under_100"] += 1
    elif 100 <= price <= 500:
        price_ranges["100_to_500"] += 1
    else:  
        price_ranges["over_500"] += 1


# Define these functions:
# - calculate_product_value(product): returns price * quantity for a product tuple
# - find_products_by_category(inventory, category): returns list of products in given category
# - apply_discount(inventory, discount_percent): returns new inventory with discounted prices
# Then use these functions to:
# - Calculate total inventory value
# - Find all "Audio" products
# - Create a new inventory with 15% discount applied
print("\n\nFunction-Based Operations:")
print("-" * 60)

def calculate_product_value(product):
    price = product[2]
    quantity = product[3]
    return price * quantity

def find_products_by_category(inventory, category):
    return [product for product in inventory if product[4] == category]

def apply_discount(inventory, discount_percent):
    discounted_inventory = []
    for product in inventory:
        discounted_price = product[2] * (1 - discount_percent / 100)
        # Create a new tuple with the discounted price, keeping other values same
        discounted_product = (product[0], product[1], discounted_price, product[3], product[4])
        discounted_inventory.append(discounted_product)
    return discounted_inventory

total_inventory_value = sum([calculate_product_value(product) for product in inventory])

audio_products = find_products_by_category(inventory, "Audio")

discounted_inventory = apply_discount(inventory, 15)


discounted_inventory = apply_discount(inventory, 15)


# TODO 18: Combine Loops, Functions, and List Operations
# Create a function generate_inventory_report(inventory) that:
# - Uses loops to analyze the inventory
# - Returns a dictionary with:
#   - 'total_products': total number of products
#   - 'total_value': sum of all (price * quantity)
#   - 'categories': list of unique categories
#   - 'low_stock': list of products with quantity < 5
#   - 'average_price': average price of all products
# Call the function and display the report
print("\n\nComprehensive Inventory Report:")
print("-" * 60)


def generate_inventory_report(inventory):
    total_products = len(inventory)
    total_value = sum([calculate_product_value(product) for product in inventory])
    categories = list(set([product[4] for product in inventory]))
    low_stock = [product for product in inventory if product[3] < 5]
    average_price = sum([product[2] for product in inventory]) / total_products
    report = {
        "total_products": total_products,
        "total_value": total_value,
        "categories": categories,
        "low_stock": low_stock,
        "average_price": average_price
    }

    return report

inventory_report = generate_inventory_report(inventory)

print= f"""
Total products: {inventory_report['total_products']}
Total inventory value: ${inventory_report['total_value']:.2f}
Categories: {inventory_report['categories']}
Low stock products: {inventory_report['low_stock']}
Average product price: ${inventory_report['average_price']:.2f}
"""