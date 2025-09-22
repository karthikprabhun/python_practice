# Variables and Data Types in Python

# Variable assignment - Primitives data types
# Immutable types
name = "Alice"         # str (string) - immutable
age = 25               # int (integer) - immutable
height = 5.7           # float (floating point number) - immutable
is_student = True      # bool (boolean) - immutable
favorite_letter = 'A'  # str (single character) - immutable

# Mutable types
hobbies = ["reading", "cycling", "music", "reading"]  # list - mutable
grades = {'math': 90, 'science': 85}       # dict (dictionary) - mutable
fruits = set(["apple", "banana", "cherry","apple"])  # set - mutable

# Print variables and their types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))
print("Hobbies:", hobbies.__repr__(), "| Type:", type(hobbies))
print("Grades:", grades.__repr__(),"value for given key is: ",grades["math"], "| Type:", type(grades))
print("Favorite Letter:", favorite_letter, "| Type:", type(favorite_letter))
print("Fruits:", fruits.__repr__(), "| Type:", type(fruits))


# Exercise:
# 1. Create your own variables for each data type shown above.
# 2. Print their values and types.
# 3. Try changing the values and see how the type changes.

fruits = ["apple", "banana", "cherry"]  # list of strings
print("Fruits:", fruits, "| Type:", type(fruits))

dictionary_example = {'name': 'Bob', 'age': 30} 
print("Dictionary Example:", dictionary_example["name"], "| Type:", type(dictionary_example))

# Immutable object (int, str, tuple)

x = 10
y = x
print("print before modification")
print("X:", x, "| id:", id(x))
print("Y:", y, "| id:", id(y))

x = x + 5

print("X:", x, "| id:", id(x)) # 15 reference changed
print("Y:", y, "| id:", id(y)) # 10

y = 15
print("Y:", y, "| id:", id(y)) # reference changed to 15 . Reference for both x and y are same point to the same object


""" At first: both x and y point to the same 10 object.

When we do x = x + 5, Python creates a new integer object 15 and moves x to reference it.

y still points to 10. """

# Mutable Object

a = [1, 2, 3]
b = a
b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

"""
a and b both point to the same list object.

When b.append(4) modifies the list, 'a' sees the change too.

In immutable types, changing the value creates a new object and changes the reference.
In mutable types, changing the value modifies the same object, so all references see the change.
"""

## No Labels = Garbage Collection
x = [1, 2, 3]
y = x

del x
del y   # Now no label points to the list

# At this point, the list object [1,2,3] has no references
# Python garbage collector can reclaim it

# Summary
# A variable in Python is just a label → reference → object. 
# Immutable objects: new objects are created when you change values.
# Mutable objects: changes affect all labels pointing to that object.
# If no label references an object → Python cleans it up (garbage collection).