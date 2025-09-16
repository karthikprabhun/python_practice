# Program demonstrating chained conditions and nested statements

def evaluate_number(num):
     if num > 0:
          print("Number is positive.")
          if num % 2 == 0:
               print("It is also even.")
          else:
               print("It is also odd.")
     elif num < 0:
          print("Number is negative.")
          if abs(num) > 100:
               print("It is less than -100.")
          else:
               print("It is greater than -100.")
     else:
          print("Number is zero.")

# Example usage
number = int(input("Enter a number: "))
evaluate_number(number)