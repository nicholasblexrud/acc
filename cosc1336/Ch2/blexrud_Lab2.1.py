# a) Nick Blexrud 
# b) status = Complete 
# c) This program is built to calculate the number of ingredients needed based on a desired serving size
# that is input by the end user
# 6db098c2d9904bb993b9caeb231a520e

# set the initial recipe ingredient amounts
RECIPE_TOMATO_SAUCE = 2.0
RECIPE_TOMATO_PASTE = .333
RECIPE_GARLIC = 2
RECIPE_OREGENO = 1

# set the initial recipe servings
RECIPE_SERVINGS = 4

# determine the single serving size by taking the initial recipe amount for each ingredient and dividing it
# by the initial serving size 
single_serving_tomato_sauce = RECIPE_TOMATO_SAUCE / RECIPE_SERVINGS
single_serving_tomato_paste = RECIPE_TOMATO_PASTE / RECIPE_SERVINGS
single_serving_garlic = RECIPE_GARLIC / RECIPE_SERVINGS
single_serving_oregeno = RECIPE_OREGENO / RECIPE_SERVINGS

# set a desired serving size variable based on input from the end user
desired_servings = float(input("Enter the number of servings of spaghetti sauce you want to make: "))

# build the output string that will display the ingredient amounts with proper formatting
desired_serving_output = f"""
To make {desired_servings} servings of spaghetti sauce, you will need:
{single_serving_tomato_sauce * desired_servings:.2f} cups of tomato sauce
{single_serving_tomato_paste * desired_servings:.2f} cups of tomato paste
{single_serving_garlic * desired_servings:.2f} cloves of garlic
{single_serving_oregeno * desired_servings:.2f} tablespoons of oregano
"""

# show the output to the end user
print(desired_serving_output)