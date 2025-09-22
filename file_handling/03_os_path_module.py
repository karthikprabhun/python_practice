import os

# change current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get the absolute path of a file
file_name = "example.txt"
abs_path = os.path.abspath(file_name)
print(f"Absolute path: {abs_path}")

# Check if a path exists
print(f"Does path exist? {os.path.exists(file_name)}")

# Check if a path is a file
print(f"Is it a file? {os.path.isfile(file_name)}")

# Check if a path is a directory
print(f"Is it a directory? {os.path.isdir(file_name)}")

# Split a path into head and tail
head, tail = os.path.split(abs_path)
print(f"Head: {head}, Tail: {tail}")

# Get the file extension
root, ext = os.path.splitext(file_name)
print(f"Root: {root}, Extension: {ext}")

# Join paths
folder = "my_folder"
joined_path = os.path.join(folder, file_name)
print(f"Joined path: {joined_path}")

# Get the directory name from a path
dir_name = os.path.dirname(abs_path)
print(f"Directory name: {dir_name}")

# Get the base name from a path
base_name = os.path.basename(abs_path)
print(f"Base name: {base_name}")

# Normalize a path (removes redundant separators)
weird_path = "my_folder//subfolder///file.txt"
normalized_path = os.path.normpath(weird_path)
print(f"Normalized path: {normalized_path}")

# Get file size (if file exists)
if os.path.exists(file_name):
     size = os.path.getsize(file_name)
     print(f"File size: {size} bytes")
else:
     print(f"{file_name} does not exist to get size.")