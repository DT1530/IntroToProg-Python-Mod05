# ----------------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries and exception handling.
# # Change Log: (Who, When, What)
#   WMcGrath,8/5/2025, Assignment05
# ----------------------------------------------------------------------------------- #
import json
from json import JSONDecodeError

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
message: str = '' # Holds the student information for the print message.
menu_choice: str  # Hold the choice made by the user.
file_obj = None  # Holds a reference to an opened file.
student_data: dict
students: list = [] # Holds combine student data in a list.

#Get the contents of Enrollments file
try:
    file_obj = open(FILE_NAME, "r")
    students = json.load(file_obj)
    file_obj.close()
    #print(students)
except FileNotFoundError as e:
    print('Error: The files was not found.')
    print('---Technical Information---')
    print(e,e.__doc__,type(e), sep='\n')
    file_obj = open(FILE_NAME, 'w')
    json.dump(students, file)
    print("The file was created since it did not exist.")
except JSONDecodeError as e:
    print("Error: Data in the JSON file is not valid.")
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep='\n')
    file_obj = open(FILE_NAME, 'w')
    json.dump(students, file)
    print("The file was reset.")
except Exception as e:
    print("Error: Something went wrong.")
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file_obj.closed:
        file_obj.close()

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name must be alphabetic.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name must be alphabetic.")
            course_name = input("Please enter the name of the course: ")
            student_data = {'FirstName': student_first_name,
                            'LastName': student_last_name,
                            'CourseName': course_name}
            students.append(student_data)
        except ValueError as e:
            print(e)
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')

    # Present the current data
    elif menu_choice == "2":
        #Present string by formatting the collected data using the print() function.
        print('Student registrations:\n')
        for student in students:
            student_first_name = student['FirstName']
            student_last_name = student['LastName']
            course_name = student['CourseName']
            message = "    {} {} is registered for {}."
            print(message.format(student_first_name, student_last_name, course_name))
        continue

    # Save the data to a file / open JSON file and write the contents of the students list
    elif menu_choice == "3":
        try:
            file_obj = open(FILE_NAME, "w")
            json.dump(students, file_obj)
            file_obj.close()
        except TypeError as e:
            print("JSON data was malformed")
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
        except Eception as e:
            print("Something went wrong.")
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file_obj.closed:
                file_obj.close()
        continue

   # Exit the program
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")