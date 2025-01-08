# a) Nick Blexrud 
# b) status = Complete 
# c) This program will open a file, store a series of numbers to it, and close the file. 
# the file.

# declare named contants
FILE_NAME = 'number_list.txt'
START_RANGE = 50
END_RANGE = 101
INCREMENT = 1

# The main function performs the program's main logic
def main():

    # write data to a file passing the named constant as argument
    write_to_a_file(FILE_NAME)

# write_to_a_file takes a file as an argument, opens, writes data to that file,
# and closes the file
def write_to_a_file(file):

    # open the file
    file = open(file, 'w')

    # iterate over the range using start, end, increment consts
    for number in range(START_RANGE, END_RANGE, INCREMENT):
        
        # write number to file
        file.write(f'{number}\n')

    #close the file
    file.close()

# call the main function
if __name__ == '__main__':
    main()