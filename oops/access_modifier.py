class Vehicle:
    def __init__(self, make, model, color):
        self.make = make # public attribute
        self.__model = model # private attribute
        self._color = color  # protected attribute

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.__model}, Color: {self._color}")


car = Vehicle("Toyota", "Camry", "Blue")

print(car.make)
# print(car.__model) accessing private attribute will throw error 
print(car._Vehicle__model) # access private var using name mangling
print(car._color) # access protected var
