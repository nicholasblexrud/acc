# a) Nick Blexrud 
# b) status = Complete 
# c) This program will generate a random floating point number between 1 and 100 which will
# be used as the radius of a circle. Then it will be passed to a function to calculate the area of the circle
# it will display the radius and the area of the circle.
# 11ccfa776b274c8b96c484573b2cc4bc

# import random, math libs
import random
import math

# set named constants
LOW_RANGE_NUMBER = 1
HIGH_RANGE_NUMBER = 100

# The main function performs the program's main logic
def main():

    # generate a random radius floating point number using Low/High range constants
    radius = random.uniform(LOW_RANGE_NUMBER, HIGH_RANGE_NUMBER)

    # pass radius into calculate area function and set returned value to area variable
    area = calculate_area(radius)

    # display the radius and the area to the end user
    print(f"The radius is: {radius}. The area is: {area}.")


# the calculate_area function takes in a radius as an argument
# and returns the area by squaring the radius and multiplying by pi
def calculate_area(radius):
    return math.pi * radius**2

# call the main function to begin the program
main()