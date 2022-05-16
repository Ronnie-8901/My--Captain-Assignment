import os
file_name = input("Enter the file name with extension : ")
file_extension = os.path.splitext(file_name)
if file_extension[1] == ".py":
    print("Python")
else:
    print("not Python")
