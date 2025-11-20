# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

#Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Coding": 125,
    "AI Research": 100,
    "Machine Learning": 200
}

# Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
customer1 = {"company_name": "Amazon", "contact_person": "Matt Brookes", "email": "mbrookes@gmail.com", "phone": "813-111-1111"}
customer2 = {"company_name": "Apple", "contact_person": "John Wick", "email": "jwick@gmail.com", "phone": "813-222-2222"}
customer3 = {"company_name": "Google", "contact_person": "Wenjie Li", "email": "wli@gmail.com", "phone": "813-333-3333"}
customer4 = {"company_name": "Nvidia", "contact_person": "Will Smith", "email": "wsmith@gmail.com", "phone": "813-444-4444"}


# Create a master customers dictionary
# Use customer IDs as keys and customer dictionaries as values
customers = {"C001": customer1, "C002": customer2, "C003": customer3, "C004": customer4}

# Display all customers
print("\nAll Customers:")
print("-" * 60)
for cid, details in customers.items():
    print(f"Customer ID: {cid}")
    print(f"Details: {details}")


# Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)
print("\n\nCustomer Lookups:")
print("-" * 60)
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer ID not found")
print(f"C002 Info: {c002_info}")
print(f"C003 Contact Person: {c003_contact}")
print(f"C999 Info: {c999_info}")

# Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information
print("\n\nUpdating Customer Information:")
print("-" * 60)
customers["C001"]["phone"] = "415-111-1111"
customers["C002"]["industry"] = "Tech"
for cid, details in customers.items():
    print(f"Customer ID: {cid}")
    print(f"Details: {details}")

# Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}
print("\n\nProject Information:")
print("-" * 60)
project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 15000}
project2 = {"name": "Cloud Migration", "service": "Data Analysis", "hours": 200, "budget": 25000}

project3 = {"name": "App Security Update", "service": "Coding", "hours": 90, "budget": 12000}

project4 = {"name": "AI Research", "service": "Data Analysis", "hours": 300, "budget": 50000}
project5 = {"name": "Ad System Optimization", "service": "AI Research", "hours": 180, "budget": 22000}

project6 = {"name": "GPU Performance Study", "service": "Machine Learning", "hours": 250, "budget": 40000}
projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4, project5],
    "C004": [project6]
}


# Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost
print("\n\nProject Cost Calculations:")
print("-" * 60)
for cid, plist in projects.items():
    for project in plist:
        service_type = project["service"]
        hourly_rate = services.get(service_type) 
        project["cost"] = hourly_rate * project["hours"]  
        print(f"Project Cost: {project['cost']}")
        print(f"Project Details: {project}")

# Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()
print("\n\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", list(customers.keys()))
company_names = [details["company_name"] for details in customers.values()]
print("Company Names:", company_names)
print("Total Number of Customers:", len(customers))

# Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts
print("\n\nService Usage Analysis:")
print("-" * 60)
service_counts = {}
for plist in projects.values():
    for project in plist:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("Service Usage Counts:")
for service, count in service_counts.items():
    print(f"{service}: {count}")

# Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)
print("\n\nFinancial Summary:")
print("-" * 60)
total_hours = 0
total_budget = 0
all_budgets = []
for plist in projects.values():
    for project in plist:
        total_hours += project["hours"]
        total_budget += project["budget"]
        all_budgets.append(project["budget"])

avg_budget = total_budget / len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)

print(f"Total Hours Across All Projects: {total_hours}")
print(f"Total Budget Across All Projects: ${total_budget:.2f}")
print(f"Average Project Budget: ${avg_budget:.2f}")
print(f"Most Expensive Project Budget: ${max_budget:.2f}")
print(f"Least Expensive Project Budget: ${min_budget:.2f}")

# Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget
print("\n\nCustomer Summary Report:")
print("-" * 60)
for cid, details in customers.items():
    customer_name = details["company_name"]
    contact_person = details["contact_person"]
    customer_projects = projects.get(cid, [])

    cust_total_hours = sum(project["hours"] for project in customer_projects)
    cust_total_budget = sum(project["budget"] for project in customer_projects)
    project_count = len(customer_projects)

    print(f"Customer ID: {cid}")
    print(f"Company Name: {customer_name}")
    print(f"Contact Person: {contact_person}")
    print(f"Number of Projects: {project_count}")
    print(f"Total Hours: {cust_total_hours}")
    print(f"Total Budget: ${cust_total_budget:.2f}")

# Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
for service, rate in adjusted_rates.items():
    print(f"{service}: {rate:.2f}")


# Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects
print("\n\nActive Customers (with projects):")
print("-" * 60)
active_customers = {cid: details for cid, details in customers.items() if projects.get(cid)}
for cid, details in active_customers.items():
    print(f"{cid}: {details['company_name']}")

# Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}
print("\n\nCustomer Budget Totals:")
print("-" * 60)
customer_budgets = {cid: sum(project["budget"] for project in plist) for cid, plist in projects.items()}
for cid, total in customer_budgets.items():
    print(f"{cid}: ${total:.2f}")


# Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension
print("\n\nService Pricing Tiers:")
print("-" * 60)
service_tiers = {
    service: ("Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic")
    for service, rate in services.items()
}
for service, tier in service_tiers.items():
    print(f"{service}: {tier}")

# Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results
print("\n\nCustomer Validation:")
print("-" * 60)
def validate_customer(customer_dict):
    """
    Checks if a customer dictionary has all required fields.

    Args:
        customer_dict (dict): Customer data with keys 'company_name', 
          'contact_person', 'email', and 'phone'.

    Returns:
        bool: True if all required fields are present and non-empty, else False.
    """
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or not customer_dict[field]:
            return False 
    return True  

for cid, customer in customers.items():
    is_valid = validate_customer(customer)
    status = "Valid" if is_valid else "Invalid"
    print(f"{cid} {customer['company_name']}: {status}")



# Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses
print("\n\nProject Status Summary:")
print("-" * 60)
projects["C001"][0]["status"] = "pending"  
projects["C001"][1]["status"] = "pending"   

projects["C002"][0]["status"] = "active"    

projects["C003"][0]["status"] = "completed" 
projects["C003"][1]["status"] = "completed" 

projects["C004"][0]["status"] = "active"


status_counts = {}
for plist in projects.values():
    for project in plist:
        status = project["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
for status, count in status_counts.items():
    print(f"{status}: {count}")


# Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys
print("\n\nDetailed Budget Analysis:")
print("-" * 60)
def analyze_customer_budgets(projects_dict):
    """
    Analyzes project budgets per customer.

    Args:
        projects_dict (dict): Dictionary mapping customer IDs to lists of projects.

    Returns:
        dict: Dictionary where keys are customer IDs, values are dictionaries with
              'total', 'average', and 'count' of budgets.
    """
    budget_stats = {}

    for cid, plist in projects_dict.items():
        total_budget = sum(project["budget"] for project in plist)
        project_count = len(plist)
        average_budget = total_budget / project_count if project_count > 0 else 0

        # Store stats for this customer
        budget_stats[cid] = {
            "total": total_budget,
            "average": average_budget,
            "count": project_count
        }

    return budget_stats

# Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations
print("\n\nService Recommendations:")
print("-" * 60)
def recommend_services(customer_id, customers, projects, services):
    """
    Recommends services to a customer based on past projects and budget.

    Args:
        customer_id (str): ID of the customer to analyze.
        customers (dict): Dictionary of customer information.
        projects (dict): Dictionary mapping customer IDs to project lists.
        services (dict): Dictionary of service rates.

    Returns:
        list: Recommended service names that the customer hasn't used yet,
              filtered by average project budget.
    """
    if customer_id not in customers:
        return [] 

    used_services = set()
    customer_projects = projects.get(customer_id, [])
    for project in customer_projects:
        used_services.add(project["service"])
    if customer_projects:
        avg_budget = sum(project["budget"] for project in customer_projects) / len(customer_projects)
    else:
        avg_budget = 0

    recommendations = []
    for service, rate in services.items():
        if service not in used_services and rate <= avg_budget:
            recommendations.append(service)

    return recommendations
