# tuple = immutable list

student = ("John", "Doe", "male", 17)

print(student.count("John"))
print(student.index("male"))

for x in student:
    print(x)

if "John" in student:
    print("John is here")
