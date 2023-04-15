# sort() method = used with lists
# sorted() function = used with iterables

students = ["Spongebob", "Patrick", "Squidward", "Mr. Krabs", "Sandy", "Plankton"]
students.sort(reverse=True) # only works with lists
for i in students:
    print(i)
print("")

students = ("Spongebob", "Patrick", "Squidward", "Mr. Krabs", "Sandy", "Plankton")
sorted_students = sorted(students, reverse=True) # works with iterables
for i in sorted_students:
    print(i)
print("")

students = [("Spongebob", "A", 28), 
            ("Patrick", "F", 27),
            ("Squidward", "C", 33),
            ("Mr. Krabs", "D", 38),
            ("Sandy", "B", 26),
            ("Plankton", "D", 31)] # list of tuples

students.sort() # sorts by first item in each tuple
for i in students:
    print(i)
print("")

grade = lambda student: student[1]
students.sort(key=grade) # sorts by second item in each tuple
for i in students:
    print(i)
print("")

age = lambda student: student[2]
students.sort(key=age) # sorts by second item in each tuple
for i in students:
    print(i)
print("")
