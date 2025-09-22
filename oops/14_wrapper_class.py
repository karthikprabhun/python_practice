# Demo wrapper class
# Wrapper is the name of the class to be wrapped. It is passes as arugment to decorator function that modifies 
# its behavior with the attributes of the passed class and returns modified class.
def decorator_function(Wrapper):
     class Wrapped(Wrapper):
          def __init__(self, *args, **kwargs):
               print("Wrapper executed before {}".format(Wrapper.__name__))
               super().__init__(*args, **kwargs)
          def display(self):
               print("Wrapper executed after {}".format(Wrapper.__name__))
               return self.name
     return Wrapped 

@decorator_function
class Wrapper:
     def __init__(self, name):
          self.name = name

obj = Wrapper("Test")
print(obj.display())