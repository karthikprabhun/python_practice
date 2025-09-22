# module: input_utils.py
def get_dimensions():
     """Prompt user for length and width, return as floats."""
     length = float(input("Enter the length: "))
     width = float(input("Enter the width: "))
     return length, width

def is_palindrome(s):
     """Check if the given string is a palindrome."""
     s = str(s).replace(" ", "").lower()
     return s == s[::-1]  