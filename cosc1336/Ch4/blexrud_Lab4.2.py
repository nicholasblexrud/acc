# a) Nick Blexrud 
# b) status = Complete 
# c) This program collects a monthly budget and a collection of expenses from the end user
# it then outputs the budget, the amount spent, and a message to the user if they are under/over budget

# set named constant
MM_PER_YEAR = 1.8

# print header
print('Year\tRise (in millimeters)')
print('---------------------------')

# iterate over the next 25 years
for year in range(1, 26):

    # calculate the rise per year using the year multiplied by the MM_PER_YEAR
    rise_per_year = year * MM_PER_YEAR

    # display the year and the rise per year, formatted
    print(f'{year}\t{rise_per_year:.2f}')