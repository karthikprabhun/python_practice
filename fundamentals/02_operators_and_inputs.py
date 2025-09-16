# operators_and_inputs.py

# Program demonstrating operators and user inputs

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic Operators
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'undefined (division by zero)'}")
print(f"{num1} % {num2} = {num1 % num2 if num2 != 0 else 'undefined (modulo by zero)'}")

# Comparison Operators
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")

# Logical Operators
print(f"Both numbers are positive: {num1 > 0 and num2 > 0}")
print(f"At least one number is positive: {num1 > 0 or num2 > 0}")
print(f"First number is not positive: {not (num1 > 0)}")