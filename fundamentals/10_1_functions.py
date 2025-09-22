## Topics covered
# Python's standard library includes a built-in function
# default, keyword, keyword only, positional, positional-only , arbitrary arguments
# variable scope i.e globals(), function annotation & modules 
# built-in functions

# Some standard built-in functions in Python:
print("Some standard built-in functions are :")
print(dir(__builtins__))  # Lists all built-in functions and exceptions

# Examples:
print(abs(-5))        # Returns absolute value
print(len("hello"))   # Returns length
print(max([1, 2, 3])) # Returns maximum value
print(sum([1, 2, 3])) # Returns sum
print(type(42))       # Returns type of object

print("----------------------------------------------------")
print("---------------------Namespace----------------------")
print("----------------------------------------------------")
""" A namespace in Python is a container that holds names (identifiers) and their corresponding objects (values, functions, classes, etc.).

It helps avoid naming conflicts by organizing names into different scopes.
Examples of namespaces: built-in namespace, global namespace (module-level), local namespace (function-level), class/object namespace. """

print("Default namespace (globals):")
print(globals())

print("demo global() & local()")
# 'x' and 'y' is defined in global namespace
x = 10
y = 'yuki'

def foo():
    z='zuki' # 'z' is in local namespace of foo()
    print(locals())
    return y

print("------------updated global namespace ---------------------------")
print(globals())

print("--------------local namespace -------------------------")
foo()

# tamper global variable in local scope
print("---------------------------------------")
print("Tamper global variable in local scope")
print("---------------------------------------")
name = 'yuki'
def tamper_globals():
    # Uncomment the following line to fix the code:
    #global name
    name = name + ' tampered'
    print("Inside tamper_globals:")
    print(globals())
    print("---------------------------------------")

# tamper_globals()
# print("After tamper_globals:")
# print(name)

""" Python uses pass by reference mechanism.
 As variable in Python is a label or reference to 
 the object in the memory, both the variables used as actual argument 
 as well as formal arguments really refer to the same object in the memory """


""" Function annotations - Function annotations describe the expected types 
for parameters and return values, making code easier to understand and maintain. They are optional and mainly used for documentation and tooling.
 """
print('---------------------------------------')
print('function annotations - what are they?')
print('---------------------------------------')
def add(x: int, y: int) -> int:
    return x + y

print(add(5, 10))
print(add.__annotations__)

print('---------------------------------------\n'
    'Types of Python Function Arguments\n'
    '1. Positional arguments:\n'
    '2. Keyword arguments:\n'
    '3. Default arguments:\n'
    '4. Variable-length arguments:\n'
    '---------------------------------------')

def positional_args(a, b):
    return a + b

# caller identifies the arguments by the parameter name
def keyword_args(a, b=5):
    return a + b

def arbitrary_args(*args):
    return sum(args)

def keyword_only_args(a, *, b):
    return a + b

def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Keyword arguments: Can be passed by name or position.")
print(keyword_args(10)) # allows positional argument i.e skip arguments
print(keyword_args(a=11, b=6)) # allows keyword arguments
print(keyword_args(b=7, a=12)) # allows out of order arguments
print(keyword_args(a=18)) # allows skipping default value

print("Keyword-only arguments: Must be passed by name, enforced by * in the function definition.")
print(keyword_only_args(10, b=5))
# print(keyword_only_args(10, 5)) # this will throw error as we are passing arguments without keyword
# posFun(6, num2=8, num3=5)

print("Arbitrary arguments:")
print(arbitrary_args(1, 2, 3))
print(arbitrary_args(4, 5, 6, 7, 8))


print('---------------------------------------')
print('arbitrary and keyword arguments')
print('---------------------------------------')

def demo_arbitrary_args(*args):
    print("Positional arguments:", args)

 #Only keyword arguments are captured; positional arguments are not.
def demo_keyword_args(**kwargs): 
    print("Keyword arguments:", kwargs)

demo_arbitrary_args(1, 2, 3)
demo_arbitrary_args("hello","world")
demo_arbitrary_args(*[4, 5, 6])
demo_arbitrary_args(*[("a","apple"),("b","banana"),("c","cherry")])

demo_keyword_args(a=1, b=2, c=3)

print('---------------------------------------')
print('arbitrary & variable length arguments are same')
print('---------------------------------------')
""" Use *args for any number of positional arguments, 
    **kwargs for any number of keyword arguments. """

def demo_variable_length(var1,*vars):
    print(var1)
    print(sum(vars))
demo_variable_length(10, 20, 30)

def demo_keyword_length(var1, **kwargs):
    print(var1)
    print(kwargs)

demo_keyword_length(10, a=1, b=2, c=3)

print('---------------------------------------')
print('modules')
print('---------------------------------------')


# import mymodule statement loads all the functions in this module in the current namespace

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("before module imported from package", dir())
print('---------------------------------------')
from MyPackage import giveFood,callYuki, giveBathToYuki,Weather

print("after module imported from package", dir())

callYuki()



