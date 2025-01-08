# a) Nick Blexrud 
# b) status = Complete 
# c) This program will create two lists, join them and perform some calculations
# before displaying those calculations to the end user.

# import dependencies
import random

# declare named contants
COUNT = 5

# The main function performs the program's main logic
def main():

    # initialize empty list
    list_one = [0] * COUNT
    list_two = [0] * COUNT

    # fill in the list with random numbers
    for number in range(COUNT):

        # assign a random number to each list using the number as the insertion index
        list_one[number] = random.randint(1,9)
        list_two[number] = random.randint(1,9)

    # join the lists
    joined_list = list_one + list_two

    # sort the list
    joined_list.sort()

    # calculate the total by passing joined list into total_list
    total = total_list(joined_list)

    # display the list, total, min, max
    print(f'''
    The list is: {joined_list}.
    The total is: {total}.
    The min is: {min(joined_list)}.
    The max is: {max(joined_list)}.
''')

# total_list takes a list as an argument, sums the values (ints)
# in the list, and returns the total
def total_list(list):
    total = 0

    for item in list:
        total += item
    
    return total

# call the main function
if __name__ == '__main__':
    main()