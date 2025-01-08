# a) Nick Blexrud 
# b) status = Complete 
# c) This program will generate a random int between 1 & 100 as the square side, and
# will calculate the area and perimeter of that square, and return it

# import random, square lib
import random
import square

# The main function performs the program's main logic
def main():

    # generate int and assign
    square_side = random.randint(1, 100)

    # pass square_side into square_area function and set variable
    square_area = square.square_area(square_side)

    # pass square_side into square_perimeter function and set variable
    square_perimeter = square.square_perimeter(square_side)

    # display the results
    print(f"""
Side Length: {square_side}
Area: {square_area}
Perimeter: {square_perimeter}
""")

# call the main function to begin the program
main()