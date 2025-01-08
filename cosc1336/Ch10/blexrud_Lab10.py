# a) Nick Blexrud 
# b) status = Complete 
# c) This program uses asks the end user for details about their employment and displays
# that information back to them
# 67f8c73144184d9fb1b0dbe26890f190

# import dependencies
import Employee

# set named constants
EMPLOYEE_COUNT = 3

# main function
def main():

    # create a list to store the employees
    employee_list = []

    # iterate over the employee count
    for count in range(EMPLOYEE_COUNT):
    
        # ask the end user to input the name, id, department, and job title
        name = input("Enter your name: ")
        id = input("Enter your id: ")
        department = input("Enter your department: ")
        job_title = input("Enter your job title: ")

        # create an instance of Employee and append to employee list
        employee_list.append(Employee.Employee(name, id, department, job_title))

        # for spacing the prompts
        print()

    # then iterate over the employee list
    for index in range(len(employee_list)):

        # print title accompanied by an index (starting at 1)
        print(f"Employee {index + 1} :", end="")

        # pass the item in the list (employee instance object) into print
        print(employee_list[index])


# Call the main function.
main()

    
