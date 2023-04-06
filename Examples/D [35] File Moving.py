# os.replace() = move a file from one location to another

import os

source = "Examples\\test3.txt"
destination = "Examples\\test\\test3.txt"

if not os.path.exists(source):
    with open (source, "w") as f:
        f.write("Hello World!\n")

if os.path.exists(destination):
    print("File already exists")
else:
    os.replace(source, destination)