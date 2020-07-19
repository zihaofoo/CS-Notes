annual_salary = float(input("Enter your annual salary: \n"))
monthly_salary = annual_salary / 12.0
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: \n"))

total_cost = float(input("Enter the cost of your dream home: \n"))
portion_down_payment = 0.25 * total_cost

semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: \n"))

current_savings = 0.0

r = 0.04

no_of_months = 0
while current_savings < portion_down_payment:
    current_savings = (current_savings * (1.0 + (r / 12.0))) + (portion_saved * monthly_salary)
    no_of_months = no_of_months + 1
    
    if (no_of_months % 6) == 0:
        annual_salary = annual_salary * (1.0 + semi_annual_raise)
        monthly_salary = annual_salary / 12.0

else:
    print("Number of months:", no_of_months)


