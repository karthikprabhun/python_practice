# Python Modules and Packages

# A module is a single Python file (.py) containing code (functions, classes, variables).
# Example: math.py is a module that provides mathematical functions.

# A package is a collection of related modules organized in a directory with an __init__.py file.
# Packages help organize code and avoid name conflicts.
# Example: numpy is a package with many modules for numerical computing.

# You import modules and packages using the 'import' statement:
# import math           # imports the math module
# from numpy import array  # imports the 'array' function from the numpy package

# Modules and packages make code reusable, organized, and easier
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MyPackage import giveFood,callYuki, giveBathToYuki,Weather

print("program to demostrate modules and package")

callYuki()

giveBathToYuki("Rin Sup-rin","Ashwini",Weather.cold)

giveFood("sunday","non veg")