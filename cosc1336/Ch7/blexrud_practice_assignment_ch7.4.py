# a) Nick Blexrud 
# b) status = Complete 
# c) This program will create a two dimensions list, then asks the end user
# for a number to assign to each element in the 2d list 
# the prints out the total
# c7324432f91544caaab239b5bb5a47e9

# declare named contants
ROWS = 4
COLUMNS = 3

# The main function performs the program's main logic
def main():

    # create 2d list
    columns = [0] * COLUMNS
    list = [
        columns, 
        columns, 
        columns, 
        columns
        ]

    # iterate over the row
    for row in range(ROWS):

        #iterate over each column
        for col in range(COLUMNS):

            # ask end user for a number
            number = int(input("enter a number: "))

            # assign number to row -> col value in the list
            list[row][col] = number

    # establish incrementor
    total = 0

    # iterate over each row
    for row in range(ROWS):

        # iterate over each column
        for col in range(COLUMNS):

            # add the value of the row -> col value to the total
            total+= list[row][col]
    
    # display the total
    print(f'The total is: {total}.')

# call the main function
if __name__ == '__main__':
    main()