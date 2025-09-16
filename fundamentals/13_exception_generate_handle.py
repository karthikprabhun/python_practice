

def simpleTryExcept():
     "Function handles an exception"
     try:
          number = int(input("Enter a number: "))
          print(f"You entered: {number}")
     except ValueError:
          print("Invalid input! Please enter a valid integer.")
     finally:
          print("Execution completed.")

 
def checkNegativeNumber(num):
     'Function generates an exception which is handled later when called in main()'
     if num < 0:
          raise Exception("This is a custom exception message.")
     else:
          print("The number is positive.")


if __name__ == "__main__":
     simpleTryExcept()
     # Exception caught in the main
     try:
          checkNegativeNumber(int(input("Enter a number to check: ")))
     except Exception as e:
          print(f"Exception caught: {e}")