# Variable = container for a value. Behaves as the value.

# Strings
firstName = "John"
lastName = "Doe"
fullName = firstName + " " + lastName

print(firstName)
print(type(firstName))

print(fullName)
print(type(fullName))

# Int
age = 13
age += 1

print(age)
print(type(age))

# Float
height = 164.59
print(height)
print(type(height))

# Boolean
human = True
print(human)
print(type(human))

# String Concatination
print("Your name is " + fullName + ". You are " + str(age) + " years old. You are " + str(height) + "cm tall. " +
      "Are you human? " + str(human) + ".")
