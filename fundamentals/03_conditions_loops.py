# Extended program to learn conditions in Python

print(" Conditions")
number = int(input("Enter a number: "))

if number > 0:
     print("The number is positive.")
elif number == 0:
     print("The number is zero.")
else:
     print("The number is negative.")

print("\nLoops")
count = int(input("Enter how many times to loop: "))

for i in range(count):
     print(f"Loop iteration {i + 1}")

print("\nWhile loop example")
n = int(input("Enter a number to countdown from: "))
while n > 0:
     print(n)
     n -= 1
print("Countdown finished.")