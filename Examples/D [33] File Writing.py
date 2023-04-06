# file writing = open(path, "w")

path = "Examples\\test.txt"
with open (path, "w") as f:
    f.write("Hello World!\n")

with open (path, "a") as f:
    print(f.write("Have a good day!\n"))