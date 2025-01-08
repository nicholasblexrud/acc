# import dependencies
import pickle

# Global constants for file name
FILE = "albums.dat"

# The save function opens the binary file
# and saves the album dictionary.
def save(albums):
    with open(FILE, "wb") as file:
        pickle.dump(albums, file)

# The retrieve function opens the binary file
# and returns the dictionary.
def retrieve():

    # try to open the saved file
    try:
        with open(FILE, "rb") as file:
            return pickle.load(file)
    
    # handle the exception if file is not found
    except FileNotFoundError:
        print("There is no saved file. Please save a file first.")