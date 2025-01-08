# a) Nick Blexrud 
# b) status = Complete 
# c) This program will ask the user for a course number and return details of the course if they exist
# otherwise it will it will print an error message and ask the user to enter another course number
# 046accd022ab421d8cec0a0593dd4f63

# The main function performs the program's main logic
def main():

    # retrieve our dicts and assign to variables
    course_rooms = get_course_rooms()
    course_instructors = get_course_instructors()
    course_times = get_course_times()

    # initiate the while loop
    course_number = True

    # as long as course_number is not stop
    while course_number != "stop":

        # ask end user for a course number
        course_number = input("Enter a course number or press enter to stop: ")

        # check if the input is stop
        if course_number == 'stop':
            # exit early
            continue

        # check if course_number exists in course_rooms
        if course_number in course_rooms:

            # display course details
            print(f"""
The details for course {course_number} are:
Room: {course_rooms[course_number]}
Instructor: {course_instructors[course_number]}
Time: {course_times[course_number]}
""")
        # otherwise display invalid course number
        else:
            print(f"{course_number} is an invalid course number.")


# get_course_rooms builds a dict of courses and rooms, and returns it
def get_course_rooms():
    dict = {}
    dict["CS101"] = "3004"
    dict["CS102"] = "4501"
    dict["CS103"] = "6755"
    dict["NT110"] = "1244"
    dict["CM241"] = "3004"
    return dict

# get_course_instructors builds a dict of courses and instructors, and returns it
def get_course_instructors():
    dict = {}
    dict["CS101"] = "Haynes"
    dict["CS102"] = "Alvarado"
    dict["CS103"] = "Rich"
    dict["NT110"] = "Burke"
    dict["CM241"] = "Lee"
    return dict

# get_course_times builds a dict of courses and times, and returns it
def get_course_times():
    dict = {}
    dict["CS101"] = "8:00 a.m."
    dict["CS102"] = "9:00 a.m"
    dict["CS103"] = "10:00 a.m."
    dict["NT110"] = "11:00 a.m."
    dict["CM241"] = "1:00 p.m."
    return dict

# call the main function
if __name__ == '__main__':
    main()