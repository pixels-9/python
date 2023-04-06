# copyfile() = copy the contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
# shutil module = a module that contains functions for copying and moving files

import shutil

path = "Examples\\test.txt"
destination = "Examples\\test2.txt"
shutil.copyfile(path, destination)
