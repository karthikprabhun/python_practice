## Topics covered
# Python's standard library includes a built-in function
# default, keyword, keyword only, positional, positional-only , arbitrary arguments
# variable scope i.e globals(), function annotation & modules 
# built-in functions

# Some standard built-in functions in Python:
print("Some standard built-in functions:")
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
print("Default namespace (globals):")
print(globals())

print("demo global() & local()")
# define global variable followed by simple function
x = 10
y = 'yuki'

def demo_global():
    z='zuki'
    print(locals())
    return y

print("---------------------------------------")
print(globals())
print("---------------------------------------")
demo_global()

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

print('---------------------------------------')
print('function annotations')
print('---------------------------------------')
def add(x: int, y: int) -> int:
    return x + y

print(add(5, 10))
print(add.__annotations__)

print('---------------------------------------')
print('arbitrary and keyword arguments')
print('---------------------------------------')

def demo_arbitrary_args(*args):
    print("Positional arguments:", args)

def demo_keyword_args(**kwargs):
    print("Keyword arguments:", kwargs)

demo_arbitrary_args(1, 2, 3)
demo_keyword_args(a=1, b=2, c=3)

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



