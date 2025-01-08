# a) Nick Blexrud 
# b) status = Complete 
# c) This program collects a monthly budget and a collection of expenses from the end user
# it then outputs the budget, the amount spent, and a message to the user if they are under/over budget
# 3e8be843b48d488b9df7884d4f7246f4

# ask user for monthly budget
monthly_budget = float(input("Enter amount budgeted for the month: "))

# set accumulator
total_spent = 0.0

# set initial state
expense_input = True

# keep asking for expenses if it's not 0
while expense_input != 0.0:
    expense_input = float(input("Enter an amount spent (0 to quit): "))

    # sum the expenses and save to total
    total_spent += expense_input

# perform calculations to determine if user is over budget and determine the difference
is_over_budget = total_spent > monthly_budget
budget_difference = abs(monthly_budget - total_spent)

# establish string output based on calculations
difference_string = "over" if is_over_budget else "under"
encouragement_text = "PLAN BETTER NEXT TIME!" if is_over_budget else "YOU'RE UNDER BUDGET - SAVE, SAVE, SAVE"

# display the message to the end user
print(f"""
Budgeted: ${monthly_budget:,.2f}
Spent: ${total_spent:,.2f}
You are ${budget_difference:,.2f} {difference_string} budget. {encouragement_text}
""")