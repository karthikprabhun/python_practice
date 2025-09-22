from enum import Enum

class Subjects(Enum):
     ENGLISH = 1
     MATH = 2
     SCIENCE = 3
     HISTORY = 4

obj = Subjects.ENGLISH
print(obj.value)
print(type(obj))

print("iterating through enum Subject:")
for sub in Subjects:
    print(sub)