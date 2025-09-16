class vector:
     def __init__(self, x, y):
          self.x = x
          self.y = y

     def __add__(self, other):
          if isinstance(other, vector):
               return vector(self.x + other.x, self.y + other.y)
          return NotImplemented

     def __sub__(self, other):
          if isinstance(other, vector):
               return vector(self.x - other.x, self.y - other.y)
          return NotImplemented

     def __mul__(self, scalar):
          if isinstance(scalar, (int, float)):
               return vector(self.x * scalar, self.y * scalar)
          return NotImplemented

     def __truediv__(self, scalar):
          if isinstance(scalar, (int, float)):
               return vector(self.x / scalar, self.y / scalar)
          return NotImplemented

     def __repr__(self):
          return f"vector({self.x}, {self.y})"
     

if __name__ == "__main__":

     print("\033[91m Demo operator overloading \033[0m")  # Red text
     v1 = vector(2, 3)
     v2 = vector(5, 7)
     print("\033[93mVector 1:\033[0m", v1)  # Yellow text
     print("\033[93mVector 2:\033[0m", v2)  # Yellow text

     print("\033[91mAddition:\033[0m", v1 + v2)  # Red text
     print("\033[93mSubtraction:\033[0m", v1 - v2)  # Yellow text
     print("\033[91mScalar Multiplication:\033[0m", v1 * 3)  # Red text
     print("\033[93mScalar Division:\033[0m", v1 / 2)  # Yellow text

print("\033[95mhow it works ?\033[0m \033[93mcommon python operators and special methods let's you overload operators, for example: __add__ for + , __sub__ for - , __mul__ for * , __truediv__ for /")