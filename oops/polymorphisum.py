class Parent():
     def display(self):
          print("Display Parent")

class Child(Parent):
     def display(self):
          print("Display Child")

child = Child()
child.display() # method from child class overridden method from parent class