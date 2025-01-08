# a) Nick Blexrud 
# b) status = Complete 
# c) This program will open a file, prints out the data that was written to it, and then close
# the file.

# declare named contants
FILE_NAME = 'students.txt'

# The main function performs the program's main logic
def main():

    # read  data from a file passing the named constant as argument
    read_from_a_file(FILE_NAME)

# read_from_a_file takes a file as an argument, opens, reads data from that file,
# and closes the file
def read_from_a_file(file):

    # open the file
    with open(file, 'r') as file:

        # print table header
        print(f'Name\tScore')
        print(f'----------------------')

        # read the first line from the file, which is the name of the first record.
        name = file.readline()

        # if a field was read, continue processing.
        while name != '':

            # read & format score
            score = float(file.readline().rstrip('\n'))

            #display name, score.
            print(f'{name.rstrip('\n')}\t{score}')

            # read the name of the next record
            name = file.readline()

# call the main function
if __name__ == '__main__':
    main()