class MyClass:
    count=0
    def __init__(self, value):
        self.value = value

    def display(self):
        print("Value:", self.value)

# Anonymous class created using type()

def setA(self, a):
    self.a = a

def getA(self):
    return self.a

Employee = type("Employee", (object,), {
    "setA": setA,
    "getA": getA,
    "sum": lambda self, x, y: x + y,
    "display": lambda self: print("Employee Name:", self.value)
})

employee = Employee()
employee.value = "John Doe"
employee.display()
print(employee.sum(10,20))
employee.setA(100)
print(employee.getA())

print("Properties of Employee --- IGNORE ---")
print(dir(Employee))
print("Properties of MyClass --- IGNORE ---")
print(dir(MyClass))