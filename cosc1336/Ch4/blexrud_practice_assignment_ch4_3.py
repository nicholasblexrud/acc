# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the end user for a positive integer and a character, and it will draw (display)
# a square using the integer and character provided.
# 14b55103bd8f4c46ae0feae2ecb53316

# set named constant
MAX_NUMBER = 15

# ask for number, character
input_number = int(input(f"Enter a positive integer no greater than {MAX_NUMBER}: "))
input_character = input("Enter a character to use to create the square: ")

# add error trap for values over max
while input_number > MAX_NUMBER:
    input_number = int(input(f"Try again. Enter a positive integer no greater than {MAX_NUMBER}: "))

# build the row
for row in range(input_number):
    # build the columns with character removing default newline break
    for col in range(input_number):
        print(input_character, end='')
    print()