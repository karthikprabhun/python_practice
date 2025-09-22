# Demo File Handling - open, write, read, close
import os, sys
# Change current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = open("example.txt", "w")  # Open a file for writing
file.write("Hello, world! \n")
file.write("Hello, world! \n")
file.write("Hello, world! \n")

file.close()

file = open("example.txt", "r")  # Open a file for reading
content = file.read()
file.close()

print(content)

file = open("example.txt", "r")
contentLine = file.readline() # Read a single line
print(contentLine)
file.close()

# Using 'with' statement - closes file automatically.
with open("example.txt", "r") as file:
    contentLine = file.readline()
    print(contentLine)

# using exception handling

try:
     file = open("example.txt", "r")
     contentLine = file.readline()
     print(contentLine)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error:", e)

import os

print("os module - check file/directory exists, create and remove directory")
os.mkdir("temp_directory")
print(os.path.exists("temp_directory"))
os.rmdir("temp_directory")

print("List files in current directory:")

print("current working directory :" , os.getcwd())

try:
    directory_path = os.getcwd()
    for file in os.listdir(directory_path):
        print(file)
except OSError as e:
   print(f"Error: Failed to list contents of directory '{directory_path}'. {e}")
