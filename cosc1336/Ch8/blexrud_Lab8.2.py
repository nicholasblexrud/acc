# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the user for a date in mm/dd/yyyy format
# and return the format in mmmm dd, yyyy
# daaebf33d7d64ee793ff2c5903d8bd09

# The main function performs the program's main logic
def main():

    # ask user for valid date
    input_date = input("Enter a date in the format mm/dd/yyyy: ")

    # split the input date
    split_date = input_date.split("/")
    
    # determine the written date
    if split_date[0] == "01":
        month = "January"
    elif split_date[0] == "02":
        month = "February"
    elif split_date[0] == "03": 
        month = "March"
    elif split_date[0] == "04":
        month = "April"
    elif split_date[0] == "05":
        month = "May"
    elif split_date[0] == "06": 
        month = "June"
    elif split_date[0] == "07":
        month = "July"
    elif split_date[0] == "08":
        month = "August"
    elif split_date[0] == "09": 
        month = "September"
    elif split_date[0] == "10":
        month = "October"
    elif split_date[0] == "11":
        month = "November"
    elif split_date[0] == "12": 
        month = "December"

    
    # display the results
    print(f"{month} {split_date[1]}, {split_date[2]}")


# call the main function
if __name__ == '__main__':
    main()