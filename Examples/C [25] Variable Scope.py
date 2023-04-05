# scope = the region of a program where a variable is visible; only available from within the region it is defined

name = "Doe"

def display_name():
    # local variable
    name = "John"
    print(name)

display_name()
print(name)