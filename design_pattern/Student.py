class Student:

     def __new__(cls, *args, **kwargs):
          print("Creating a new instance...")
          instance = super(Student,cls).__new__(cls)
          return instance

     def __init__(self, name, age):
          print("Initializing instance...")
          self.name = name
          self.age = age

     def display(self):
          print(f"Name: {self.name}, Age: {self.age}" )

if __name__ == "__main__":
     s1 = Student("Karthik", 43)
     s1.display()

""" 
__new__() creates the object (rarely overridden).
__init__() initializes the object (commonly used).
 """

