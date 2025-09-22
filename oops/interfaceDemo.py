from abc import ABC, abstractmethod

class Animal(ABC):
     @abstractmethod
     def speak(self):
          pass

class Dog(Animal):
     def speak(self):
          print("Woof!")

     def pradeepFunction(self):
          AmOuT = 100
          print("This is Pradeep's function in Dog class.")

class Cat(Animal):
     def speak(self):
          print("Meow!")

# Usage
animals = [Dog(), Cat()]
for animal in animals:
     animal.speak()

     if isinstance(animal, Dog):
          animal.pradeepFunction()