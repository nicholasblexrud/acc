# a) Nick Blexrud 
# b) status = Complete 
# c) This program will prompt the user to specify the number of random number to generate
# it will then open a file, write the desired count of random numbers, and close the file. 

# import supporting libs
import random

# declare named contants
FILE_NAME = 'number_list.txt'
LOOP_START_RANGE = 1
START_RANDOM_RANGE = 1
END_RANDOM_RANGE = 501

# The main function performs the program's main logic
def main():

    try:
        # ask user for input
        end_range = int(input('Please specify how many random numbers: '))

        # write data to a file passing the named constant as argument
        write_to_a_file_given_range(FILE_NAME, end_range)
    
    # handle file errors
    except IOError:
        print('An error occured trying to read the file.')

    # handle value errors
    except ValueError:
        print('Non-numeric data found in the file.')

    # handle all other errors
    except:
        print('An error occured')

# write_to_a_file_given_range takes a file and end range as arguments, 
# opens, writes data to that file, and closes the file
def write_to_a_file_given_range(file, end_range):

    # open the file
    file = open(file, 'w')

    # iterate over the range using const start, argument end_range plus 1 to make inclusive, 
    for number in range(LOOP_START_RANGE, end_range + 1):

        # generate a random number within a range
        random_number = random.randrange(START_RANDOM_RANGE, END_RANDOM_RANGE)
        
        # write random number to file
        file.write(f'{random_number}\n')

    #close the file
    file.close()

# call the main function
if __name__ == '__main__':
    main()