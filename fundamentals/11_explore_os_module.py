import os

os.environ["apikey"]="12345"  # Set environment variable
os.environ["apicreationtime"]="2024-10-10"  # Set another environment variable
print("current directory is",os.getcwd)  # Get current working directory
print(os.getenv("apikey") )
print(os.getenv("apicreationtime") )


pid = os.getpid()  # Get current process ID
ppid = os.getppid()  # Get parent process ID
print(f"process id is {pid} and parent process id is {ppid}")

# Read a file using os.open and os.read
file_path = os.getcwd() + '/samples/books.xml'
fd = os.open(file_path, os.O_RDONLY)  # Open file for reading
content = os.read(fd, 100)  # Read up to 100 bytes
os.close(fd)  # Close the file descriptor
print("File content:", content.decode())
