import os

# Get current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# List files and directories in current directory
items = os.listdir(cwd)
print(f"Items in '{cwd}': {items}")

# Create a new directory
new_dir = "demo_dir"
if not os.path.exists(new_dir):
     os.mkdir(new_dir)
     print(f"Directory '{new_dir}' created.")
else:
     print(f"Directory '{new_dir}' already exists.")

# Rename the directory
renamed_dir = "renamed_demo_dir"
if os.path.exists(new_dir):
     os.rename(new_dir, renamed_dir)
     print(f"Directory renamed to '{renamed_dir}'.")

# Remove the directory
if os.path.exists(renamed_dir):
     os.rmdir(renamed_dir)
     print(f"Directory '{renamed_dir}' removed.")

env_vars = os.environ
# Create environment variable
env_vars.__setattr__('myvariable', 'myvalue') #This didnt work
# Get environment variables
print("Some environment variables:")
for key in list(env_vars)[:5]:
     print(f"{key}: {env_vars[key]}")

# Join paths
path1 = "folder"
path2 = "file.txt"
full_path = os.path.join(path1, path2)
print(f"Joined path: {full_path}")

# Check if a path exists
print(f"Does '{full_path}' exist? {os.path.exists(full_path)}")