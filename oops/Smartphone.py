class Smartphone:

     def __init__(self, brand, model, price):
         self.__brand = brand
         self.__model = model
         self.__price = price

     def display_info(self):
         print(f"Brand: {self.__brand}")
         print(f"Model: {self.__model}")
         print(f"Price: {self.__price}")

     def get_brand(self):
          return self.__brand

     def set_brand(self, brand):
          self.__brand = brand

     def get_model(self):
          return self.__model

     def set_model(self, model):
          self.__model = model

     def get_price(self):
          return self.__price

     def set_price(self, price):
          if price > 0:
               self.__price = price
          else:
               print("Invalid price. Price must be positive.")

# print("Class is blueprint for creating objects. It has state and behavior.")
# iPhone17Obj = Smartphone("Apple", "iPhone 17", 1200)
# iPhone17Obj.display_info()

# iPhone17Obj.set_price(1900)
# print("Updated Price:")
# print(f'iPhone17Obj.get_price(): {iPhone17Obj.get_price()}')

# iPhone17Obj.price = 1000
# print(f'price value after direct update: {iPhone17Obj.get_price()}')
# print(f'this works becz object invoked from outside the class.')

