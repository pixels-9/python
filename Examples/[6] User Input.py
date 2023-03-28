name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age + 1

print("Hello " + name + "!", end="\n\n")
print("Happy Birthday!", end="\n\n")
print("You are now " + str(age) + " years old!", end="\n\n")
print("You are " + str(height) + "cm tall!")
