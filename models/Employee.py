class Employee:
     def __init__(self, emp_id, name, department, salary):
          self.emp_id = emp_id
          self.name = name
          self.department = department
          self._salary = salary

     @property
     def salary(self):
          return self._salary
     
     @salary.setter
     def salary(self,value):
          if value < 0:
               raise ValueError("Salary cannot be zero")
          self._salary=value

     def display_info(self):
          print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}")

     def update_salary(self, new_salary):
          self.salary = new_salary
          print(f"Salary updated to {self.salary}")

     def change_department(self, new_department):
          self.department = new_department
          print(f"Department changed to {self.department}")

# Include self as the first parameter in every instance method definition.
# When you call the method (e.g., obj.method()), Python automatically passes the instance as self.
# You do not need to pass self explicitly when calling the method—only when defining it.