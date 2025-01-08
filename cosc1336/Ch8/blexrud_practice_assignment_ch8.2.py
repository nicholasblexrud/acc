# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the end user to enter a sentence and it will 
# convert any uppercase letter to lowercase, and convent any lowercase letter
# to uppercase. It will print the original and new sentences.
# 65abdba9ff2f43afb906c48953f5bb66

# The main function performs the program's main logic
def main():
        # ask user to enter a sentence
    sentence = input("Enter a sentence: ")

    # create new accumulator
    new_sentence = ""

    # iterate over the sentence
    for letter in sentence:

        # check if letter is upper case
        if letter.isupper():

            # convert to lower, and assign
            letter = letter.lower()
        
        # check if letter is lower case
        elif letter.islower():

            # convert to upper, and assign
            letter = letter.upper()

        # append letter to new sentence 
        new_sentence+= letter
    
    # display the results
    print(f"""
sentence: {sentence}
new sentence: {new_sentence}
""")

# call the main function
if __name__ == '__main__':
    main()