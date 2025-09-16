import os

sample_dir=os.path.join(os.getcwd(),'samples')
json_file_path=os.path.join(sample_dir,'books.json')
bin_file_path=os.path.join(sample_dir,'books.bin')
txt_file_path=os.path.join(sample_dir,'books.txt')


print("Demo write file operation \n")
bytes = b'\x42\x6f\x6f\x6b\x73\x20\x42\x69\x6e\x61\x72\x79\x20\x44\x61\x74\x61'
print("of type :",type(bytes))

def write_binary_file(bytes_data):
     with open(bin_file_path, 'wb') as f: # 'wb' means write binary
          f.write(bytes)

def write_text_file(text_data):
    with open(txt_file_path, 'w') as f: # 'w' means write text
        f.write(text_data)

message = 'hello, in the era of super intelligence i am still learning \'hello world\' program'

if __name__ == "__main__":
    write_binary_file(bytes)
    write_text_file(message)


# File I/O in Python
#Concept covered - with, open() , read and write both binary and non-binary file

def read_file(filepath):
     with open(filepath, 'r', encoding='utf-8', buffering=8192) as f: # mode 'r' means read text
          return f.read()

def read_BinaryFile(filepath):
     with open(filepath, 'rb') as f: # mode 'rb' means read binary
          return f.read()

print("--------------------------------------")
print("json file has",read_file(json_file_path))
print("--------------------------------------")
print("binary file has",read_BinaryFile(bin_file_path))
print("--------------------------------------")
print("text file has",read_file(txt_file_path))



