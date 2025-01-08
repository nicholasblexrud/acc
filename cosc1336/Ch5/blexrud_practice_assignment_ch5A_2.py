# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the user the number of kilometers they would like to convert to miles,
# perform a calculation, and then display a message to converted miles.

# set global constant
CONVERSION_FACTOR = 0.6214

# The main function performs the program's main logic
def main():
    
    # ask the user for number of kilometers
    kilometers = float(input('Please enter the number of kilometers you would like to convert: '))

    # perform the conversion and display the converted number to the end user
    convert_km_to_miles(kilometers=kilometers)

def convert_km_to_miles(kilometers):
    converted_to_miles = kilometers * CONVERSION_FACTOR
    print(f'The conversion to miles yielded: {converted_to_miles:,.2f} miles.')

# call the main function to begin the program
main()