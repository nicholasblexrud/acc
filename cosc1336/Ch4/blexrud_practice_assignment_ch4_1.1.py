# a) Nick Blexrud 
# b) status = Complete 
# c) This program will keep asking the end user for a number in the range of 1-7, and displays the day of the week.
# if the user enters a value outside of 1-7, then it will display an error message. If the user enters 0 it will 
# terminate the program.

input_number = int(input("Enter a number in the range of 1-7 or enter 0 to stop: "))

while input_number != 0:
    if input_number == 1:
        result = "Monday"
    elif input_number == 2:
        result = "Tuesday"
    elif input_number == 3:
        result = "Wednesday"
    elif input_number == 4:
        result = "Thursday"
    elif input_number == 5:
        result = "Friday"
    elif input_number == 6:
        result = "Saturday"
    elif input_number == 7:
        result = "Sunday"
    else:
        result = "Error: invalid value entered. Please try again."
    
    print(result)

    input_number = int(input("Enter another number in the range of 1-7 or enter 0 to stop: "))
