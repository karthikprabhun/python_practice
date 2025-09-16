# The Student class models a student with attributes for name, age, and grade.
# It demonstrates object-oriented principles such as encapsulation and provides
# examples of attribute access, modification, and introspection using built-in methods.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.grade})"

if __name__ == "__main__":
    

    s1 = Student("Alice", 20, "A")
    s2 = Student("Bob", 22, "B")
    print(s1)
    print(s2)

    s1.age = 21
    print("object s1 attribute age updated:", s1)

    print("Instead of updating the object directly, consider using a method to update attributes.")

    s1.__setattr__('age', 23) # setattr(s1, 'age', 23)
    print("object s1 attribute age updated using setattr and retrived using __getattribute__:", s1.__getattribute__('age'))

     # Built-in class attributes i.e __dict__, __class__, __module__ etc
    print("Built-in class attributes:", dir(s1))
    print("object s1 attribute __dict__:", s1.__dict__)
    print("object s1 attribute __class__:", s1.__class__)
    print("object s1 attribute __module__:", s1.__module__)

    print("object s1 type:", type(s1.age))
