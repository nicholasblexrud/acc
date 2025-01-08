# a) Nick Blexrud 
# b) status = Complete 
# c) This program asks the end user for the cost of a hamburger, fries and shake. 
# It then takes those values and calculates a total cost and an average cost with an appropriate message.

cost_of_hamburger = float(input("Enter the cost for the hamburger: "))
cost_of_fries = float(input("Enter the cost for the fries: "))
cost_of_shake = float(input("Enter the cost for the shake: "))

TOTAL_NUMBER_OF_ITEMS = 3

# add-up the costs of each item
total_cost = cost_of_hamburger + cost_of_fries + cost_of_shake
print(f"The total cost is: ${total_cost:,.2f}")

# divide the total cost by the total number of items
avg_cost = total_cost/TOTAL_NUMBER_OF_ITEMS
print(f"The average cost is: ${avg_cost:,.2f}")

