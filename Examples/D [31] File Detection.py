# os module = a module that contains functions for interacting with the operating system

import os

path = "Examples\\test.txt"
if os.path.exists(path):
    print("Location exists")
    if os.path.isfile(path):
        print("Location is a file")
    elif os.path.isdir(path):
        print("Location is a directory")
else:
    print("Location does not exist")