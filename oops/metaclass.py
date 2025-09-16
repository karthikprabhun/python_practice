class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, attrs)
    
class myClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value

    def display(self):
        print("Value:", self.value)

if __name__ == "__main__":
    obj = myClass(42)
    obj.display()

print("Metaclass is a class  whose instances are classes. it defines how classes are created and behave.")

""" Quick Analogy

Think of it like this:

object = “the ultimate ancestor” (like Adam/Eve in mythology).

type = “the factory” that makes all classes.

All classes (like int, str, Dog) are made by type, and all of them inherit from object. """