# a) Nick Blexrud 
# b) status = Complete 
# c) This program will open a file and count the upper, lower, digits, and spaces,
# and return the display the counts back to the end user.

# The main function performs the program's main logic
def main():

    # set acculumators for the four counts
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_space = 0

    # open the file
    with open('text.txt', 'r') as file:

        # read the lines
        lines = file.readlines()

        # iterate over the lines
        for line in lines:

            # iterate over each letter in each line
            for letter in line:

                # increment count if letter is upper
                if letter.isupper():
                    count_upper += 1
                
                # increment count if letter is lower
                if letter.islower():
                    count_lower += 1
                
                # increment count if letter is digit
                if letter.isdigit():
                    count_digit += 1
                
                # increment count if letter is space
                if letter.isspace():
                    count_space += 1
    
    # display the results
    print(f"""
Uppercase letters: {count_upper}
Lowercase letters: {count_lower}
Digits: {count_digit}
Spaces: {count_space}
""")


# call the main function
if __name__ == '__main__':
    main()