# a) Nick Blexrud 
# b) status = Complete 
# c) This program will open a file, iterate over its contents, perform a calculation to 
# derive a sum and average, and then close
# the file.
# b3bf0247d25c433ba113939b4945957a

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
            counter = 0
            sum = 0

            # iterate over the lines in the file
            for line in file:

                # increment the counter by 1 to store # of lines for avg calc
                counter += 1

                # add the numbers up
                sum += int(line.rstrip('\n'))

            # perform calculation to obtain average
            average = sum / counter

            #display the sum and the average, formatted
            print(f'The sum is: {sum:,.2f}. The average is: {average:,.2f}.')
    
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