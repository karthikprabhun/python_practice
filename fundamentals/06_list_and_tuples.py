# Real-time example: Managing a shopping cart using lists and tuples

# Tuples: Used for immutable product information (name, price)
product1 = ("Apple", 0.5)
product2 = ("Banana", 0.3)
product3 = ("Milk", 1.2)

# List: Used for mutable shopping cart (can add/remove items)
shopping_cart = []

# Add products to cart (as tuples)
shopping_cart.append(product1)
shopping_cart.append(product2)
shopping_cart.append(product3)

# Display cart contents
print("Shopping Cart Contents:")
for item in shopping_cart:
    print(f"Product: {item[0]}, Price: ${item[1]}")

# Remove an item (e.g., remove Banana)
shopping_cart.remove(product2)

print("\nUpdated Shopping Cart:")
for item in shopping_cart:
    print(f"Product: {item[0]}, Price: ${item[1]}")
    print({item})

# Calculate total price
total = sum(item[1] for item in shopping_cart)
print(f"\nTotal Price: ${total}")

# Explanation:
# - Tuples are used for product info because product name and price shouldn't change.
# - List is used for the shopping cart because items can be added or removed.
# - This demonstrates how lists and tuples are used together in real-world scenarios.

## Tuples - another example
mobile = [(1, "apple"),(2, "orange"),(3, "grape")]

mobile.insert(4,(4,"kiwi"))

print(mobile)

mobile.remove((3, "grape"))

for val in mobile:
    print(val[1])

# Sets - no dublicate values

alpha = set(["a","b","c","d"])
alpha.add("b")
print(alpha)

beta =set(["a","x","z","d"])
print("Intersect",alpha.intersection(beta))


#Dictionaries
person = {"name": "Varun", "age": 32, "location": "Mangalore"}
person["email"] = 'hello@mail.com'

print("iterate over keys\n")
for key in person.keys():
    print(key)

print("iterate over values\n")
for value in person.values():
    print(value)

print("iterate over both keys and values\n")
for key, value in person.items():
    print("key:", key, "val:", value)
    print(f"{key}: {value}")

def print_map_items(map_obj):
    for key, value in map_obj.items():
        print(f"{key}: {value}")
