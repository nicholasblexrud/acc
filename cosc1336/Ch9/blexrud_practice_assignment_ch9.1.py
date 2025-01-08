# a) Nick Blexrud 
# b) status = Complete 
# c) This program uses asks the end user for details about their pet and displays
# that information back to them

# import dependencies
import cosc1336.Ch10.Pet as Pet

# main function
def main():
    
    # ask the end user to input the name, type and age
    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of pet you have: ")
    age = input("Enter the age of your pet: ")

    # create an instance of pet and assign input to variable my_pet
    my_pet = Pet.Pet(name, animal_type, age)

    # display the data back to the end user
    print(f"""
{my_pet.get_name()} is a {my_pet.get_animal_type()} and is {my_pet.get_age()} years old.
""")


# Call the main function.
main()

    
