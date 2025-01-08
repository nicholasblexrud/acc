# a) Nick Blexrud 
# b) status = Complete 
# c) This program asks the end user for a monthly gross income and monthly paycheck deductions. It then calculates
# the net monthly income, yearly gross pay, yearly net pay, and outputs an appropriate calculation for each.

monthly_gross_income = float(input("Enter your monthly gross income: "))
monthly_deductions = float(input("Enter your monthly paycheck deductions: "))
MONTHS_IN_YEAR = 12

# subtract the monthly deductions from monthly gross income
net_monthly_income = monthly_gross_income - monthly_deductions
print(f"Monthly net income is: ${net_monthly_income:,.2f}")

# multiply monthly gross income by the number of months in the year
yearly_gross_pay = monthly_gross_income * MONTHS_IN_YEAR
print(f"Yearly gross pay is: ${yearly_gross_pay:,.2f}")

# multiply monthly net income by the number of months in the year
yearly_net_pay = net_monthly_income * MONTHS_IN_YEAR
print(f"Yearly net pay is: ${yearly_net_pay:,.2f}")
