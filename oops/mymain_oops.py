from Smartphone import Smartphone

print("Demo OOPS principles - encapsulation")

samsung = Smartphone("Samsung", "Galaxy S23", 999)
samsung.display_info()

samsung.__price = 10222
print(f'price attribue value after direct modifcation  samsung.get_price(): {samsung.get_price()}')

samsung.set_price(10431)
print(f'price attribue value using setter method samsung.set_price(): {samsung.get_price()}')

print(f'So price attribue value modified only using setter but not directly i.e encapsulation achived: {samsung.get_price()}')