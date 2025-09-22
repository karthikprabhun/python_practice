class Singleton:
     _instance = None  #  class variable, all object will share same instance

     def __new__(cls, *args, **kwargs):
          if not cls._instance:
               cls._instance = super(Singleton, cls).__new__(cls)
          return cls._instance

     def __init__(self, value=None):
          if not hasattr(self, 'initialized'):
               self.value = value
               self.initialized = True
          else:
               print("Singleton instance already initialized.")  

# Example usage
if __name__ == "__main__":
     print("Creating Singleton instances...")
     s1 = Singleton(10)
     print("Instance created __new__() and initialized __init__() with value 10.")
     print("Create another object of type Singleton class...")
     s2 = Singleton(20) # This will not create a new instance i.e __new__ will return the existing instance
     print("logic with in __init__ not executed ")
     print(s1.value)  # Output: 10
     print(s2.value)  # Output: 10
     print(s1 is s2)  # Output: True
     print(id(s1), id(s2))  # Output: Same ID