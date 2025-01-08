# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the end user for first, middle, last name
# then it will count the number of a's, e's, and s's before displaying back to user.

# declare named contants


# The main function performs the program's main logic
def main():

    # ask for first, middle, last names
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")

    # concate the names together
    full_name = first_name + middle_name + last_name

    # set acculumators for the three counts
    count_a = 0
    count_e = 0
    count_s = 0

    # iterate over full name
    for letter in full_name:

        # increment count if a or A
        if letter == 'a' or letter == 'A':
            count_a += 1
        
        # increment count if e or E
        if letter == 'e' or letter == 'E':
            count_e += 1
        
        # increment count if s or S
        if letter == 's' or letter == 'S':
            count_s += 1
    
    # display the results
    print(f"""
# of A's: {count_a}
# of E's: {count_e}
# of S's: {count_s}
""")


# call the main function
if __name__ == '__main__':
    main()