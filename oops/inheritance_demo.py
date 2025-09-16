class Parent:
     def __init__(self , parentAttribute):
          print("parent class constructor trigged / initialized")
          self.parentAttribute = parentAttribute


     def display_parent_info(self):
          print(f"Parent Attribute: {self.parentAttribute}")

     def setParentAttribute(self, value):
          self.parentAttribute = value

     def getParentAttribute(self):
          return self.parentAttribute
     
class Child(Parent):
     def __init__(self, parentAttribute, childAttribute):
          super().__init__(parentAttribute)
          self.childAttribute = childAttribute
          print("child class constructor trigged / initialized")

     def display_child_info(self):
          print(f"Child Attribute: {self.childAttribute}")

     def display_both_parent_child_info(self):
          self.display_parent_info()
          self.display_child_info()

# Instance of child
print("-----------------------------------------")
child = Child("Parent Value", "Child Value")
child.display_parent_info() # method inherited from parent class
child.display_child_info() # method from child class

print("-----------------------------------------")
child.setParentAttribute("New Parent Value")
child.display_both_parent_child_info()