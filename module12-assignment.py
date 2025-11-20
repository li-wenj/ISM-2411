# Module 12 Assignment: Business Analytics Fundamentals and Applications
# GreenGrocer Data Analysis

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Welcome message
print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO CREATE SAMPLE DATA (DO NOT MODIFY) -----
# Set seed for reproducibility
np.random.seed(42)

# Store information
stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}

# Create store dataframe
store_df = pd.DataFrame(store_data)

# Product categories and departments
departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

# Generate sales data for each store
sales_data = []
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Base performance factors for each store (relative scale)
store_performance = {
    "Tampa": 1.0, 
    "Orlando": 0.85, 
    "Miami": 1.2, 
    "Jacksonville": 0.75, 
    "Gainesville": 0.65
}

# Base performance factors for each department (relative scale)
dept_performance = {
    "Produce": 1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery": 0.95,
    "Prepared Foods": 1.1
}

# Generate daily sales data for each store, department, and category
for date in dates:
    # Seasonal factor (higher in summer and December)
    month = date.month
    seasonal_factor = 1.0
    if month in [6, 7, 8]:  # Summer
        seasonal_factor = 1.15
    elif month == 12:  # December
        seasonal_factor = 1.25
    elif month in [1, 2]:  # Winter
        seasonal_factor = 0.9
    
    # Day of week factor (weekends are busier)
    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0  # Weekend vs weekday
    
    for store in stores:
        store_factor = store_performance[store]
        
        for dept in departments:
            dept_factor = dept_performance[dept]
            
            for category in categories[dept]:
                # Base sales amount
                base_sales = np.random.normal(loc=500, scale=100)
                
                # Calculate final sales with all factors and some randomness
                sales_amount = base_sales * store_factor * dept_factor * seasonal_factor * dow_factor
                sales_amount = sales_amount * np.random.normal(loc=1.0, scale=0.1)  # Add noise
                
                # Calculate profit margin (different base margins for departments)
                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery": 0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]
                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)  # Keep within reasonable range
                
                # Calculate profit
                profit = sales_amount * profit_margin
                
                # Add record
                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })

# Create sales dataframe
sales_df = pd.DataFrame(sales_data)

# Generate customer data
customer_data = []
total_customers = 5000

# Age distribution parameters
age_mean, age_std = 42, 15

# Income distribution parameters (in $1000s)
income_mean, income_std = 85, 30

# Create customer segments (will indirectly influence spending)
segments = ["Health Enthusiast", "Gourmet Cook", "Family Shopper", "Budget Organic", "Occasional Visitor"]
segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]

# Store preference probabilities (matches store performance somewhat)
store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami": 0.30,
    "Jacksonville": 0.15,
    "Gainesville": 0.10
}

for i in range(total_customers):
    # Basic demographics
    age = int(np.random.normal(loc=age_mean, scale=age_std))
    age = max(min(age, 85), 18)  # Keep age in reasonable range
    
    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])
    
    income = int(np.random.normal(loc=income_mean, scale=income_std))
    income = max(income, 20)  # Minimum income
    
    # Customer segment
    segment = np.random.choice(segments, p=segment_probabilities)
    
    # Preferred store
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))
    
    # Shopping behavior - influenced by segment
    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8, 15)  # Visits per month
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120, scale=25)
    elif segment == "Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150, scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:  # Occasional Visitor
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)
    
    # Ensure values are reasonable
    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket = max(avg_basket, 15)
    
    # Loyalty tier based on combination of frequency and spending
    monthly_spend = visit_frequency * avg_basket
    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"
    
    # Add to customer data
    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000,  # Convert to actual income
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth": visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(visit_frequency * avg_basket, 2),
        "LoyaltyTier": loyalty_tier
    })

# Create customer dataframe
customer_df = pd.DataFrame(customer_data)

# Create some calculated operational metrics for stores
operational_data = []

for store in stores:
    # Get store details
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]
    
    # Calculate store metrics
    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"] == store]["Profit"].sum()
    
    # Calculate derived metrics
    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(5, np.random.normal(loc=4.0, scale=0.3) * 
                                (store_performance[store] ** 0.5))
    
    # Add to operational data
    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft, 2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })

# Create operational dataframe
operational_df = pd.DataFrame(operational_data)

# Print data info
print("\nDataframes created successfully. Ready for analysis!")
print(f"Sales data shape: {sales_df.shape}")
print(f"Customer data shape: {customer_df.shape}")
print(f"Store data shape: {store_df.shape}")
print(f"Operational data shape: {operational_df.shape}")

# Print sample of each dataframe
print("\nSales Data Sample:")
print(sales_df.head(3))
print("\nCustomer Data Sample:")
print(customer_df.head(3))
print("\nStore Data Sample:")
print(store_df)
print("\nOperational Data Sample:")
print(operational_df)
# ----- END OF DATA CREATION -----


# TODO 1: Descriptive Analytics - Overview of Current Performance
# 1.1 Calculate and display basic descriptive statistics for sales and profit
# REQUIRED: Store results in variables for testing
def analyze_sales_performance():
    """
    Analyze overall sales performance with descriptive statistics
    REQUIRED: Create and return dictionary with keys:
    - 'total_sales': float
    - 'total_profit': float
    - 'avg_profit_margin': float
    - 'sales_by_store': pandas Series
    - 'sales_by_dept': pandas Series
    """
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    avg_profit_margin = sales_df["ProfitMargin"].mean()

    sales_by_store = sales_df.groupby("Store")["Sales"].sum()
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum()

    return {
        "total_sales": float(round(total_sales, 2)),
        "total_profit": float(round(total_profit, 2)),
        "avg_profit_margin": float(round(avg_profit_margin, 4)),
        "sales_by_store": sales_by_store,
        "sales_by_dept": sales_by_dept
    }
# 1.2 Create visualizations showing sales distribution by store, department, and time
# REQUIRED: Return matplotlib figures
def visualize_sales_distribution():
    """
    Create visualizations showing how sales are distributed
    REQUIRED: Return tuple of three figures (store_fig, dept_fig, time_fig)
    """
    store_fig = plt.figure()
    sales_by_store = sales_df.groupby("Store")["Sales"].sum()
    sales_by_store.plot(kind="bar", title="Total Sales by Store", ylabel="Sales ($)", rot=0)

    dept_fig = plt.figure()
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum()
    sales_by_dept.plot(kind="bar", title="Total Sales by Department", ylabel="Sales ($)", rot=20)

    time_fig = plt.figure()
    daily_sales = sales_df.groupby("Date")["Sales"].sum()
    daily_sales.plot(title="Daily Sales Trend", ylabel="Sales ($)")

    return store_fig, dept_fig, time_fig

# 1.3 Analyze customer segments and their spending patterns
# REQUIRED: Return analysis results
def analyze_customer_segments():
    """
    Analyze customer segments and their relationship to spending
    REQUIRED: Return dictionary with keys:
    - 'segment_counts': pandas Series
    - 'segment_avg_spend': pandas Series
    - 'segment_loyalty': pandas DataFrame
    """

    segment_counts = customer_df["Segment"].value_counts()

    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean()

    segment_loyalty = (
        customer_df
        .groupby(["Segment", "LoyaltyTier"])
        .size()
        .reset_index(name="Count")
    )

    return {
        "segment_counts": segment_counts,
        "segment_avg_spend": segment_avg_spend,
        "segment_loyalty": segment_loyalty
    }

# TODO 2: Diagnostic Analytics - Understanding Relationships
# 2.1 Identify factors correlated with sales performance
# REQUIRED: Return correlation results
def analyze_sales_correlations():
    """
    Analyze correlations between various factors and sales performance
    REQUIRED: Return dictionary with keys:
    - 'store_correlations': pandas DataFrame
    - 'top_correlations': list of tuples (factor, correlation)
    - 'correlation_fig': matplotlib figure
    """
    numeric_cols = [
        "AnnualSales",
        "AnnualProfit",
        "SalesPerSqFt",
        "SalesPerStaff",
        "InventoryTurnover",
        "CustomerSatisfaction"
    ]

    store_correlations = operational_df[numeric_cols].corr()

    # Correlation with AnnualSales (excluding itself)
    annual_sales_corr = store_correlations["AnnualSales"].drop("AnnualSales")

    # Sort by absolute correlation, highest first
    top_correlations = sorted(
        annual_sales_corr.items(),
        key=lambda x: abs(x[1]),
        reverse=True
    )

    # Visualization: scatter of AnnualSales vs SalesPerSqFt
    x = operational_df["SalesPerSqFt"]
    y = operational_df["AnnualSales"]

    correlation_fig = plt.figure()
    plt.scatter(x, y)
    plt.xlabel("Sales Per Sq Ft")
    plt.ylabel("Annual Sales")
    plt.title("Sales Per Sq Ft vs Annual Sales")

    return {
        "store_correlations": store_correlations,
        "top_correlations": top_correlations,
        "correlation_fig": correlation_fig
    }

# 2.2 Compare stores based on operational metrics
# REQUIRED: Return comparison results
def compare_store_performance():
    """
    Compare stores across different operational metrics
    REQUIRED: Return dictionary with keys:
    - 'efficiency_metrics': pandas DataFrame (with SalesPerSqFt, SalesPerStaff)
    - 'performance_ranking': pandas Series (ranked by profit)
    - 'comparison_fig': matplotlib figure
    """

    efficiency_metrics = operational_df.set_index("Store")[["SalesPerSqFt", "SalesPerStaff"]]

    performance_ranking = (
        operational_df
        .set_index("Store")["AnnualProfit"]
        .sort_values(ascending=False)
    )

    comparison_fig = plt.figure()
    efficiency_metrics["SalesPerSqFt"].plot(kind="bar", title="Sales Per Sq Ft by Store", ylabel="Sales ($)", rot=0)

    return {
        "efficiency_metrics": efficiency_metrics,
        "performance_ranking": performance_ranking,
        "comparison_fig": comparison_fig
    }

# 2.3 Analyze seasonal patterns and their impact
# REQUIRED: Return seasonal analysis
def analyze_seasonal_patterns():
    """
    Identify and visualize seasonal patterns in sales data
    REQUIRED: Return dictionary with keys:
    - 'monthly_sales': pandas Series
    - 'dow_sales': pandas Series (day of week)
    - 'seasonal_fig': matplotlib figure
    """
    monthly_sales = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()

    dow_sales = sales_df.groupby(sales_df["Date"].dt.dayofweek)["Sales"].sum()

    seasonal_fig = plt.figure()
    monthly_sales.plot(title="Monthly Sales Trend", xlabel="Month", ylabel="Sales ($)")

    return {
        "monthly_sales": monthly_sales,
        "dow_sales": dow_sales,
        "seasonal_fig": seasonal_fig
    }

# TODO 3: Predictive Analytics - Basic Forecasting
# 3.1 Create a simple linear regression model to predict store sales
# REQUIRED: Return model results
def predict_store_sales():
    """
    Use linear regression to predict store sales based on store characteristics
    REQUIRED: Return dictionary with keys:
    - 'coefficients': dict (feature: coefficient)
    - 'r_squared': float
    - 'predictions': pandas Series
    - 'model_fig': matplotlib figure
    """
    x = operational_df["SalesPerSqFt"]
    y = operational_df["AnnualSales"]

    slope, intercept = np.polyfit(x, y, 1)

    predictions = intercept + slope * x
    predictions_series = pd.Series(predictions, index=operational_df["Store"])

    y_mean = y.mean()
    ss_total = ((y - y_mean) ** 2).sum()
    ss_resid = ((y - predictions) ** 2).sum()
    r_squared = 1 - (ss_resid / ss_total)

    model_fig = plt.figure(figsize=(8, 5))
    plt.scatter(y, predictions)
    plt.xlabel("Actual Annual Sales")
    plt.ylabel("Predicted Annual Sales")
    plt.title("Actual vs Predicted Store Annual Sales")
    plt.tight_layout()

    coefficients = {
        "Intercept": intercept,
        "SalesPerSqFt": slope
    }

    return {
        "coefficients": coefficients,
        "r_squared": float(r_squared),
        "predictions": predictions_series,
        "model_fig": model_fig
    }

# 3.2 Forecast departmental sales trends
# REQUIRED: Return forecast results
def forecast_department_sales():
    """
    Analyze and forecast departmental sales trends
    REQUIRED: Return dictionary with keys:
    - 'dept_trends': pandas DataFrame
    - 'growth_rates': pandas Series
    - 'forecast_fig': matplotlib figure
    """

    sales_df["Month"] = sales_df["Date"].dt.month

    months = sorted(sales_df["Month"].unique())
    departments = sorted(sales_df["Department"].unique())

    dept_trends = pd.DataFrame(index=months, columns=departments)

    for dept in departments:
        dept_monthly = (
            sales_df[sales_df["Department"] == dept]
            .groupby("Month")["Sales"]
            .sum()
        )
        dept_trends[dept] = dept_monthly

    dept_trends = dept_trends.fillna(0)

    first_month = dept_trends.index.min()
    last_month = dept_trends.index.max()

    first_sales = dept_trends.loc[first_month]
    last_sales = dept_trends.loc[last_month]

    growth_rates = (last_sales - first_sales) / first_sales.replace(0, 1)

    forecast_fig = plt.figure()
    for dept in departments:
        plt.plot(dept_trends.index, dept_trends[dept], label=dept)

    plt.title("Department Sales Trends by Month")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()

    return {
        "dept_trends": dept_trends,
        "growth_rates": growth_rates,
        "forecast_fig": forecast_fig
    }


# TODO 4: Integrated Analysis - Business Insights and Recommendations
# 4.1 Identify the most profitable combinations of store, department, and customer segments
# REQUIRED: Return opportunity analysis
def identify_profit_opportunities():
    """
    Identify the most profitable combinations and potential opportunities
    REQUIRED: Return dictionary with keys:
    - 'top_combinations': pandas DataFrame (top 10 store-dept combinations)
    - 'underperforming': pandas DataFrame (bottom 10)
    - 'opportunity_score': pandas Series (by store)
    """
    combo_profit = (
        sales_df
        .groupby(["Store", "Department"])["Profit"]
        .sum()
        .reset_index()
    )

    top_combinations = combo_profit.sort_values("Profit", ascending=False).head(10)

    underperforming = combo_profit.sort_values("Profit", ascending=True).head(10)

    ops = operational_df.set_index("Store")

    opportunity_score = (
        (ops["CustomerSatisfaction"].max() - ops["CustomerSatisfaction"]) +
        (ops["SalesPerSqFt"].max() - ops["SalesPerSqFt"]) +
        (ops["AnnualProfit"].max() - ops["AnnualProfit"])
    )

    return {
        "top_combinations": top_combinations,
        "underperforming": underperforming,
        "opportunity_score": opportunity_score
    }

# 4.2 Develop recommendations for improving performance
# REQUIRED: Return list of recommendations
def develop_recommendations():
    """
    Develop actionable recommendations based on the analysis
    REQUIRED: Return list of at least 5 recommendation strings
    """
    recommendations = [
        "Underperforming stores like Gainesville and Jacksonville should receive more support through better staffing, stronger marketing, and improved inventory management to help raise their overall sales.",
        "High-profit departments such as Prepared Foods and Produce should be expanded in top-performing stores like Miami and Tampa to take advantage of strong customer demand.",
        "The company should create targeted promotions for customer groups like Family Shoppers and Gourmet Cooks, since these segments have the highest average monthly spending.",
        "Because weekend sales are higher than weekday sales, stores should increase staffing levels and make sure products remain stocked during weekends to meet customer needs.",
        "Lower-performing stores should focus on improving the customer experience by offering fresher products, faster checkout times, and better overall service to increase satisfaction."
    ]

    return recommendations

# TODO 5: Summary Report
# REQUIRED: Generate comprehensive summary
def generate_executive_summary():
    """
    Generate an executive summary of key findings and recommendations
    REQUIRED: Print executive summary with sections:
    - Overview (1 paragraph)
    - Key Findings (3-5 bullet points)
    - Recommendations (3-5 bullet points)
    - Expected Impact (1 paragraph)
    """
    print("Overview:")
    print("This report analyzes GreenGrocer’s sales, customer behavior, and store performance "
          "to understand how well each store and department is doing. The goal was to use data "
          "to identify what is working well and what needs improvement. By looking at sales "
          "patterns, customer spending habits, and store operations, the analysis helps explain "
          "why certain locations perform better than others and where the company has the most "
          "opportunities to grow.\n")

    print("Key Findings:")
    print("- Miami and Tampa are the strongest stores, showing the highest annual sales and consistent performance.")
    print("- Prepared Foods and Produce are the most profitable departments across multiple locations.")
    print("- Customer groups like Family Shoppers and Gourmet Cooks spend the most each month and bring strong value.")
    print("- Weekend sales are noticeably higher than weekday sales, showing clear demand patterns.")
    print("- Some store and department combinations, especially in Gainesville and Jacksonville, are underperforming and need improvement.\n")

    print("Recommendations:")
    print("- Support lower-performing stores through better staffing, stronger marketing, and improved inventory management.")
    print("- Expand high-profit departments such as Prepared Foods and Produce in top stores to increase overall revenue.")
    print("- Create targeted promotions for Family Shoppers and Gourmet Cooks since they spend more than other segments.")
    print("- Increase weekend staffing and make sure products remain stocked to match higher weekend demand.")
    print("- Improve customer experience in lower-performing stores by focusing on fresher products, better service, and faster checkout times.\n")

    print("Expected Impact:")
    print("If these recommendations are followed, GreenGrocer should see stronger sales, higher customer satisfaction, "
          "and more balanced performance across all stores. Improving underperforming areas while expanding high-profit "
          "departments will help the company grow and operate more efficiently. These changes are expected to support "
          "long-term success and help the business better meet customer needs.\n")

# Main function to execute all analyses
# REQUIRED: Do not modify function name
def main():
    print("\n" + "=" * 60)
    print("GREENGROCER BUSINESS ANALYTICS RESULTS")
    print("=" * 60)
    
    # Execute analyses in a logical order
    # REQUIRED: Store all results for potential testing
    
    print("\n--- DESCRIPTIVE ANALYTICS: CURRENT PERFORMANCE ---")
    sales_metrics = analyze_sales_performance()
    dist_figs = visualize_sales_distribution()
    customer_analysis = analyze_customer_segments()
    
    print("\n--- DIAGNOSTIC ANALYTICS: UNDERSTANDING RELATIONSHIPS ---")
    correlations = analyze_sales_correlations()
    store_comparison = compare_store_performance()
    seasonality = analyze_seasonal_patterns()
    
    print("\n--- PREDICTIVE ANALYTICS: FORECASTING ---")
    sales_model = predict_store_sales()
    dept_forecast = forecast_department_sales()
    
    print("\n--- BUSINESS INSIGHTS AND RECOMMENDATIONS ---")
    opportunities = identify_profit_opportunities()
    recommendations = develop_recommendations()
    
    print("\n--- EXECUTIVE SUMMARY ---")
    generate_executive_summary()
    
    # Show all figures
    plt.show()
    
    # Return results for testing purposes
    return {
        'sales_metrics': sales_metrics,
        'customer_analysis': customer_analysis,
        'correlations': correlations,
        'store_comparison': store_comparison,
        'seasonality': seasonality,
        'sales_model': sales_model,
        'dept_forecast': dept_forecast,
        'opportunities': opportunities,
        'recommendations': recommendations
    }

# Run the main function
if __name__ == "__main__":
    results = main()