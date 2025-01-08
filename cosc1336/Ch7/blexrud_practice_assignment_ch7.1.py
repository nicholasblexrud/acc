# a) Nick Blexrud 
# b) status = Complete 
# c) This program will generate a list of lottery numbers and then print out each number in the list.
# 4da36182486344509365f8d9474bb47c

# import dependencies
import random

# declare named contants
LOTTERY_NUMBER_COUNT = 7

# The main function performs the program's main logic
def main():

    # initialize empty list
    lottery_numbers = [0] * LOTTERY_NUMBER_COUNT

    # fill in the list with random numbers to generate a lottery ticket
    for number in range(len(lottery_numbers)):

        # generate a random number between 1-9
        random_number = random.randint(1,9)

        # assign the random number to the list using the number as the insertion index
        lottery_numbers[number] = random_number
    
    # iterate over the list and print out the lottery numbers
    for number in lottery_numbers:
        print(f'Lottery number is: {number}')


# call the main function
if __name__ == '__main__':
    main()