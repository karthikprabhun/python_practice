num = 10
print("every object implicitly inherit object class ", isinstance(num, object))

name = "Yuki"
print("every object implicitly inherit or subclass of object class ", issubclass(name.__class__, object))

# type is the class of all classes

s = "hello"
print("The type of s is:", type(s))

print(type(int))  # <class 'type'>
print(type(str))  # <class 'type'>

# ==========================================================
# 1. Basics of Python OOP
# ==========================================================
#
# - `object` is the base class for all classes in Python.
#   Every class implicitly inherits from `object`.
#
# - `type` is the metaclass for all classes.
#   It is responsible for creating all classes, including `object` itself.
# ==========================================================

# ==========================================================
# 2. Key Facts
# ==========================================================
#
# 1. Every class in Python is an instance of type.
# ==========================================================
print(isinstance(int, type))
print(isinstance(float, type))
print(isinstance(object, type))  # Even object itself is created by type.
print(isinstance(str, type))
print(isinstance(list, type))
print(isinstance(dict, type))
print(isinstance(type, type))

# Thus any class is an instance of type.

# 2. Every object in Python ultimately inherits from object
print(isinstance(10, object))    # True
print(isinstance("hi", object))  # True
print(isinstance(int, object))   # True (classes are objects too!)

# 3. And here’s the twist:
#    object is an instance of type.
#    type is a subclass of object.
#
#    object → type → object

# ==========================================================
# 3. Demonstration of Circularity
# ==========================================================
print(type(object))  # <class 'type'> Which means object itself was constructed by type.
print(type(type))    # <class 'type'>

print(isinstance(object, type))  # True
print(isinstance(type, object))  # True
print(issubclass(type, object))  # True

# this shows :
# object is made by type. i.e Which means object itself was constructed by type.
# type itself is an object, so it inherits from object.i.e type is subclass of object.

""" Refined Summary

✔️ type → metaclass that creates classes.

✔️ object → base class for all classes.

✔️ object is instance of type.

✔️ type is subclass of object, and instance of itself.

This is the circular relationship that makes Python’s object model consistent. """