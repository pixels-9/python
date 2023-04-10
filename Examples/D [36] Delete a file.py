# os.remove() = delete a file
# os.rmdir() = delete a directory
# shutil.rmtree() = delete a directory and all its contents

import os
import shutil

path = "Examples\\test3.txt"
if not os.path.exists(path):
    with open (path, "w") as f:
        f.write("Hello World!\n")

try:
    os.remove(path)
    # os.rmdir(path)
    # shutil.rmtree(path)
except PermissionError:
    print("Permission denied")
except OSError:
    print("Cannot delete that with that function")

