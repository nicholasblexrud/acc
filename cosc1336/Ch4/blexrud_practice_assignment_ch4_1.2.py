# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the end user to enter in two numbers, it will sum the numbers and display the result. 
# After the result has been displayed, it will ask the user if they wish to perform the operation again
# where they then can either enter 'Yes' to continue or 'No' to terminate the program.

# set initial condition to get into the loop
keep_running = 'Yes'

while keep_running != 'No':
    
    # ask for the two numbers
    first_input_number = int(input("Enter in your first number: "))
    second_input_number = int(input("Enter in your second number: "))

    # sum the first and second number inputs
    calculated_sum = first_input_number + second_input_number

    # display the sum as output
    print(f"The sum of your two numbers is: {calculated_sum:,.0f}") 

    # ask if the user wants to run again
    keep_running = input("Do you wish to perform the operation again? Type 'Yes' or 'No': ")