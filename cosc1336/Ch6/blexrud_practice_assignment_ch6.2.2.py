# a) Nick Blexrud 
# b) status = Complete 
# c) This program will open a file, print out the data that was written to it, perform a calculation, and then close
# the file.
# f29f6f4284bc4dac9959ac33fe95ecaf

# declare named contants
FILE_NAME = 'number_list.txt'

# The main function performs the program's main logic
def main():

    # read  data from a file passing the named constant as argument
    read_from_a_file(FILE_NAME)

# read_from_a_file takes a file as an argument, opens, reads data from that file,
# and closes the file
def read_from_a_file(file):

    # open the file
    file = open(file, 'r')

    # iterate over the lines in the file
    for line in file:

        #display the number with newline removed
        print(f'{line.rstrip('\n')}')

    # close the file
    file.close()

# call the main function
if __name__ == '__main__':
    main()