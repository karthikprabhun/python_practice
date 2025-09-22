import sys
import os

# Ensure that the 'models' module is in the same directory as this script or in your Python path.
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import geometry
import input_utils
from models import Employee


def main():
    # length, width = input_utils.get_dimensions()
    # area = geometry.calculate_area(length, width)
    # print(f"The area of the rectangle is {area}")

    # name = str(input("Enter the string to check for palindrome"))
    # print("Is palindrome",input_utils.is_palindrome(name))

    emp = Employee.Employee(101, "John Doe", "Engineering", 1000)
    print(f"Employee Name: {emp.name}, ID: {emp.emp_id}, Department: {emp.department}")

    emp._salary = 100
    print("update Salary is ", emp.salary)

    emp.update_salary(1800)

    emp.display_info


if __name__ == "__main__":
    main()

    print(dict())
