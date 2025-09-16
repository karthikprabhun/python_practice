
import geometry
import input_utils

name="Yuki"
print(name.capitalize()) #string values are stored as Unicode internally by default utf-8
print(name.encode(encoding="utf-16",errors="strict")) 
print(name.encode(encoding="utf-32",errors="strict")) 

def aiAssistanceSystem():
     print("I am system")

def aiAssistanceUser():
     return "I am user"

def aiAssistanceAdmin():
     val="I am Admin"
     return val

aiAssistanceSystem()
print(aiAssistanceUser())
print(aiAssistanceAdmin())


print('area for given input is : ',geometry.calculate_area(30,40))
input_utils.is_palindrome("naveen")
vals = input_utils.get_dimensions()
print(vals)

