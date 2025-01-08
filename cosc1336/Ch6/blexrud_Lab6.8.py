# a) Nick Blexrud 
# b) status = Complete 
# c) This program will open a file, iterate over its contents, perform a calculation to 
# derive a sum, average and count, and then close the file. 
# 3aa2165af2144773bf6f9c394f29659c

# declare named contants
FILE_NAME = 'number_list.txt'

# The main function performs the program's main logic
def main():

    # read  data from a file passing the named constant as argument
    read_from_a_file(FILE_NAME)

# read_from_a_file takes a file as an argument, opens, reads data from that file,
# and closes the file
def read_from_a_file(file):

    try:
        # open the file
        with open(file, 'r') as file:

            # set local variables
            count = 0
            sum = 0

            # iterate over the lines in the file
            for line in file:

                # increment the count by 1 to store # of lines for avg calc
                count += 1

                # add the numbers up
                sum += int(line.rstrip('\n'))

            # perform calculation to obtain average
            average = sum / count

            #display the sum, average, and count, formatted
            print(f'''
                  The total is: {sum:,.0f}. 
                  The average is: {average:,.2f}.
                  The count of numbers is: {count:,.0f}.
                  ''')
    
    # handle file errors
    except IOError:
        print('An error occured trying to read the file.')

    # handle value errors
    except ValueError:
        print('Non-numeric data found in the file.')

    # handle all other errors
    except:
        print('An error occured')


# call the main function
if __name__ == '__main__':
    main()