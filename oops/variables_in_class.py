# Variables / attribute scope in class - Class vs Instance variable
# Class variables are shared among all instances.
# Instance variables are unique to each instance.
# Changing company on an instance creates a new instance variable; 
# changing it on the class affects all instances.

class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

# Create two instances
e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # Output: TechCorp
print(e2.company)  # Output: TechCorp


e1.company = "OtherCorp"  # This creates an instance variable 'company' for e1
print(e1.company)  # Output: OtherCorp
print(e2.company)  # Output: TechCorp

e1.origin = "India" # In python, attribute can be defined without declaration in __init__
print(e1.name)  # Output: Alice
print(e2.name)  # Output: Bob

print(e1.origin)  # Output: India
# print(e2.origin)  # throws error as origin is not defined

# Changing the class variable directly
Employee.company = "GlobalTech"
print(e1.company)  # Output: OtherCorp (instance variable shadows class variable)
print(e2.company)  # Output: GlobalTech (class variable changed)

