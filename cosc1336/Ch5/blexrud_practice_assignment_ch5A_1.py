# a) Nick Blexrud 
# b) status = Complete 
# c) This program will display to the user the purpose of the program (to make a sandwhich), a series of steps
# on how to make a sandwhich, and an exit message.
# f32400806c0a466b8db14d331d869de8

# The main function performs the program's main logic
def main():

    # Display the start-up message
    startup_message()
    input('Press Enter to see Step 1.')

    # Display step 1
    step1()
    input('Press Enter to see Step 2.')

    # Display step 2
    step2()
    input('Press Enter to see Step 3.')

    # Display step 3
    step3()
    input('Press Enter to see Step 4.')

    # Display step 4
    step4()

    # Display the exit message
    exit_message()

def startup_message():
    print('This program tells you how to make a sandwhich.')
    print('There are 4 steps in the process.')
    print()

def step1():
    print('Step 1: Take out two pieces of bread, open the jam, and open the peanut butter.')
    print()

def step2():
    print('Step 2: Spread the jam on one side of the bread.')
    print('Spread the peanut butter on the other side of the bread.')
    print()

def step3():
    print('Step 3: Put the two piece of bread together.')
    print()

def step4():
    print('Step 4: Eat the sandwhich')
    print()

def exit_message():
    print('You have made a sandwhich. Goodbye.')

# call the main function to begin the program
main()