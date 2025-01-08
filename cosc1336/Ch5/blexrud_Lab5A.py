# a) Nick Blexrud 
# b) status = Complete 
# c) This program calculates an score and number of stars a restarant should receive based upon
# five critic's reviews
# 17c65385dc3d40f385d01418de08c403

# set named constants
MAX_NUMBER_OF_RATINGS = 5

# The main function performs the program's main logic
def main():

    # set accumulator
    total = 0

    # loop through max number of ratings
    for rating_num in range(MAX_NUMBER_OF_RATINGS):

        # ask the user for the critics rating and assign to rating variable
        rating = float(input("Enter critic's score between 0 and 10: "))

        # input validation to check if number is between 1 and 10, inclusive
        while not (rating >= 0 and rating <= 10):
            # again, ask the user for a valid critics rating
            rating = float(input("Try again. Enter critic's score between 0 and 10: "))
        
        # add the rating to the total
        total += rating
    
    # calculate the numeric average
    avg_rating = total / MAX_NUMBER_OF_RATINGS
    
    # display the average and the number of stars
    determine_stars(avg_rating)

# determine_stars function takes the average rating of the scores as an argument
# and determines the number of stars, and then prints a message
def determine_stars(avg_rating):
    if avg_rating >= 9:
        number_of_stars = "*****"
    elif avg_rating < 9 and avg_rating >= 8:
        number_of_stars = "****"
    elif avg_rating < 8 and avg_rating >= 7:
        number_of_stars = "***"
    elif avg_rating < 7 and avg_rating >= 6:
        number_of_stars = "**"
    elif avg_rating < 6 and avg_rating >= 5:
        number_of_stars = "*"
    else:
        number_of_stars = "No stars"
    
    # display message to end user with their average rating and number of stars
    print(f'Your score of {avg_rating:,.2f} gives you {number_of_stars}')

# call the main function to begin the program
main()