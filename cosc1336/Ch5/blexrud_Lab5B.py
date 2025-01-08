# a) Nick Blexrud 
# b) status = Complete 
# c) This program prints a table that displays the distance an object has fallen
# over a specific amount of time

# import additional libs
import distance

# declare named contants
START_SECOND = 1
END_SECOND = 11

# The main function performs the program's main logic
def main():

    # print the header of the output table
    print('Time\tFalling Distance')
    print('----------------------')

    # iterate over the range using the named constants for start/end
    for second in range(START_SECOND, END_SECOND):

        # display each row listing the second and the calculated distance
        print(f'{second}\t{distance.falling_distance(second):,.2f}')

# call the main function to begin the program
main()