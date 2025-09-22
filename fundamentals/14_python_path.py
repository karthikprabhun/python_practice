import sys
import os
""" 
The Python path is a list of directories that Python searches to find 
modules and packages when you use an import statement.
"""

print("List of python paths are", sys.path)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ["PYTHONPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

print("after update --> List of python paths are", sys.path)

print(os.environ["PYTHONPATH"])


