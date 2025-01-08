# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the user for 10 numbers and a search number to compare against those 10 numbers
# it will determine what input numbers are greater than the search number and retun both the 
# original list and the filtered list
# ac332ee09564480688d372e86226b0ff

# declare named contants
NUMBER_OF_INTEGERS = 10

# The main function performs the program's main logic
def main():

    # set iterator
    count = 0

    # create empty list
    list = [0] * NUMBER_OF_INTEGERS

    # Display a simple message telling the user to enter numbers
    print(f"Enter a list of {NUMBER_OF_INTEGERS} integers")

    # continue until we've reached desired number of integers
    while count < NUMBER_OF_INTEGERS:

        # ask end user for integer
        input_integer = int(input("Enter a number: "))

        # assign input int to list index
        list[count] = input_integer

        # increment the count
        count += 1
    
    # ask for the search number
    search_number = int(input("Enter the number you wish to test"
                              "if the list elements are greater than: "
                            ))

    # assign output of display larger to filtered_list
    filtered_list = display_larger(list, search_number)

    # display the results
    print(f"List of numbers:")
    print(f"{list}")
    print(f"List of number that are larger than {search_number}:")
    print(f"{filtered_list}")

# display_larger take a list and search number as arguments, and returns a filtered list based on
# a conditional check that compares each element to the search number
def display_larger(list, search_number):
    return [item for item in list if item > search_number]

# call the main function
if __name__ == '__main__':
    main()