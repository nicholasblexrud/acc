# a) Nick Blexrud 
# b) status = Complete 
# c) This program will open a file, store data to it, and close the file. Then it will open that file
# print out the data that was written to it, perform a calculation, and then close
# the file.

# declare named contants
FILE_NAME = 'my_name.txt'

# The main function performs the program's main logic
def main():

    # write data to a file passing the named constant as argument
    write_to_a_file(FILE_NAME)

    # read  data from a file passing the named constant as argument
    read_from_a_file(FILE_NAME)

# write_to_a_file takes a file as an argument, opens, writes data to that file,
# and closes the file
def write_to_a_file(file):

    # open the file
    file = open(file, 'w')

    # write data to the file
    file.write("Nick Blexrud\n")
    file.write("Jimi Hendrix\n")
    file.write("37\n")

    #close the file
    file.close()

# read_from_a_file takes a file as an argument, opens, reads data from that file,
# and closes the file
def read_from_a_file(file):

    # open the file
    file = open(file, 'r')

    # set local variables by advancing through the file and removing \n
    my_name = file.readline().rstrip('\n')
    other_name = file.readline().rstrip('\n')
    my_age = int(file.readline().rstrip('\n'))

    # set local variable for calculated age
    my_age_divided_by_two = my_age / 2

    # display output to user
    print(f'My name is: {my_name}')
    print(f'My other name is: {other_name}')
    print(f'My age is: {my_age}. My age divided by two is: {my_age_divided_by_two}.')

    file.close()

# call the main function
if __name__ == '__main__':
    main()