
import geometry
import input_utils

name="Yuki"
print(" capitalized name:", name.capitalize()) #string values are stored as Unicode internally by default utf-8
print(" name after enncoding: utf-16", name.encode(encoding="utf-16",errors="strict")) 
print(" name after enncoding: utf-32", name.encode(encoding="utf-32",errors="strict")) 

def aiAssistanceSystem():
     print("I am system")

def aiAssistanceUser():
     return "I am user"

def aiAssistanceAdmin():
     val="I am Admin"
     return val

# function calls - in the same module and imported modules
aiAssistanceSystem()
print(aiAssistanceUser())
print(aiAssistanceAdmin())
print('area for given input is : ',geometry.calculate_area(30,40))

print("input_utils.is_palindrome(\"naveen\"):", input_utils.is_palindrome("naveen"))

print("input_utils.get_dimensions():",  input_utils.get_dimensions())

