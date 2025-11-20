#welcome message
print("=" * 60)
print("FASTFUNDS FINANCIAL - BUSINESS LOAN EVALUATION SYSTEM")
print("=" * 60)

business_name = "TechSolutions Inc."
years_in_operation = 3.5
annual_revenue = 280000
credit_score = 690
requested_amount = 150000
business_type = "Technology"  

#displaying application details
print(f"\nLOAN APPLICATION DETAILS:")
print(f"Business Name: {business_name}")
print(f"Years in Operation: {years_in_operation:.1f} years")
print(f"Annual Revenue: ${annual_revenue:,.2f}")
print(f"Credit Score: {credit_score}")
print(f"Requested Loan Amount: ${requested_amount:,.2f}")
print(f"Business Type: {business_type}")
print("\nPROCESSING APPLICATION...")

#initialize and check if the business meets basic requirements
meets_basic_requirements = True
eligibility_reasons = []
if years_in_operation < 2 :
    meets_basic_requirements = False
    eligibility_reasons.append("Business must be in operation for at least 2 years.")
if annual_revenue < 100000 :
    meets_basic_requirements = False
    eligibility_reasons.append("Annual revenue must be at least $100,000.")
if credit_score < 600 :
    meets_basic_requirements = False
    eligibility_reasons.append("Credit score must be at least 600.")
if requested_amount < 25000 or requested_amount > 500000 :
    meets_basic_requirements = False 
    eligibility_reasons.append("Requested loan amount must be between $25,000 and $500,000.")

#risk assesment
risk_tier = "Very High Risk"
if meets_basic_requirements :
    risk_tier = "High Risk"
    if years_in_operation >= 3 and credit_score >= 650 and annual_revenue >= 150000 :
        risk_tier = "Medium Risk"
        if years_in_operation >= 5 and credit_score >= 720 and annual_revenue >= 300000 :
            risk_tier = "Low Risk"

#implementing loan amount approval rules
if risk_tier == "Low Risk" or risk_tier == "Medium Risk" :
    max_loan_amount = float(annual_revenue * 0.8)
elif risk_tier == "High Risk" :
    max_loan_amount = float(annual_revenue * 0.5)
else :
    max_loan_amount = float(annual_revenue * 0.25)

#check if business meets industry specific requirements
passes_industry_check = True
industry_reasons = []
if business_type == "Technology" :
    if years_in_operation < 3 and credit_score < 700 :
        passes_industry_check = False
        industry_reasons.append("Technology businesses with less than 3 years in operation must have a credit score of at least 700")
elif business_type == "Retail" :
    if years_in_operation < 3 and requested_amount > 150000:
        passes_industry_check = False
        industry_reasons.append("Retail businesses must have at least 3 years in operation to qualify for more than $150000")
elif business_type == "Service" :
    if credit_score < 650 and requested_amount > 200000 :
        passes_industry_check = False
        industry_reasons.append("Service businesses must have a credit score of at least 650 to qualify for more than $200000")
elif business_type == "Manufacturing" :
    if annual_revenue < 250000 :
        passes_industry_check = False
        industry_reasons.append("Manufacturing businesses must have annual revenue of at least $250000")

#determine interest rates based on risk tier and business type
if risk_tier == "Low Risk" :
    interest_rate = float(6)
elif risk_tier == "Medium Risk" :
    interest_rate = float(8)
elif risk_tier == "High Risk" :
    interest_rate = float(10.5)
else :
    interest_rate = float(13)
if business_type == "Technology" :
    interest_rate = interest_rate - 0.5
elif business_type == "Manufacturing" and years_in_operation < 3 :
    interest_rate = interest_rate + 0.5

#final decision with reasons
final_reasons = []
final_recommendations = []
if not passes_industry_check or not meets_basic_requirements:
    decision = "DENIED"
    if not passes_industry_check :
        final_reasons.extend(industry_reasons)
        final_recommendations.append("Make sure you meet the basic industry specific requirements")
    if not meets_basic_requirements :
        final_reasons.extend(eligibility_reasons)
        final_recommendations.append("Make sure you meet the basic eligibility requirements")
elif requested_amount <= max_loan_amount :
    decision = "APPROVED"
    approved_amount = float(requested_amount)
    final_reasons.append("You have passed the basic eligibility and industry specific rules and your requested loan amount is below our maximum cap based on your risk tier")
else :
    decision = "CONDITIONALLY APPROVED"
    approved_amount = float(max_loan_amount)
    final_reasons.append("You have passed the basic eligibility and industry specific rules but your requested loan amount exceeds our maximum cap based on your risk tier")
    final_recommendations.append("Make sure your requested loan amount is reasonable and corresponds with your risk tier")

print("=====LOAN DECISION=====")
print(f"Decision: {decision}")
print(f"Risk Assessment: {risk_tier}")
print("\nLoan Details:")
print(f"- Requested Amount: ${requested_amount}")
print(f"- Approved Amount: ${approved_amount}")
print(f"- Interest Rate: {interest_rate}%")
print("\nReasons:")
print(final_reasons)
print("\nRecommendations:")
print(final_recommendations)