# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the end user to enter in a low number and a high number, it will display a table 
# of the iterator number and the number (10X) multiplied by 10, it will then sum all of the numbers and display a total

# set named constants
MULTIPLIER = 10

# ask for low, high numbers
low_input_number = int(input("Enter in your low number: "))
high_input_number = int(input("Enter in your high number: "))

# set accumulator
total = 0

# print table header
print("Number\t10X")
print("--------------------")

# loop over the range established by low, high inputs
for num in range(low_input_number, high_input_number):

    # display the number and the number multiplied by the multiplier constant, seperated by a tab
    print(f"{num}\t{(num * MULTIPLIER)}")

# loop over the range established by low, high inputs
for num in range(low_input_number, high_input_number):

    # using augmented assignment for addition
    total += num

print(f"\n\nTotal: {total}")