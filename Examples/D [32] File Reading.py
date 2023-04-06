# file reading = open(path, "r")
# with open(path, "r") as varName: = a way to open a file and close it automatically

path = "Examples\\test.txt"
try:
    with open(path) as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)
    print("File does not exist")

print(f.closed)
