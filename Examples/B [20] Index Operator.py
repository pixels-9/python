# index operator = gives access to a sequence's elements by their position (str, list, tuple, dict)

name = "John Doe"
first_name = name[0:4].upper()
last_name = name[5:].lower()


if name[0] == "J":
    print("The first letter is J")

print(name)
print(first_name)
print(last_name)
