def displayInfo(name, age):
    print("Value received:", id(name), " of type ", type(name),'has value', name)
    print("Value received:", id(age), " of type ", type(age),'has value', age)

# Call the function with keyword arguments where order of parameter doesn't matter
displayInfo(age=5, name="Hello")

print('Arbitrary or Variable-length Arguments')

