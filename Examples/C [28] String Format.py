# str.format() = an optional method that allows for more control over the formatting of strings

animal = "cow"
item = "moon"
name = "John"
number = 1000

print("The {} jumped over the {}".format(animal, item)) # default formatting
print("The {1} jumped over the {0}".format(animal, item)) # 0 and 1 are the indexes of the arguments
print("The {a} jumped over the {a}".format(a=animal, i=item)) # a and i are the identifiers of the arguments

text = "The {} jumped over the {}"
print(text.format(animal, item)) # default formatting

print("Hello, my name is {}. Nice to meet you!".format(name)) # default formatting
print("Hello, my name is {:10}. Nice to meet you!".format(name)) # 10 spaces of padding after the name
print("Hello, my name is {:<10}. Nice to meet you!".format(name)) # 10 spaces of padding before the name
print("Hello, my name is {:^10}. Nice to meet you!".format(name)) # 10 spaces of padding before and after the name
print("Hello, my name is {:l^10}. Nice to meet you!".format(name)) # 10 ls of padding before and after the name

print("The number is {:.3f}".format(number)) # 3 decimal places
print("The number is {:,}".format(number)) # comma separator
print("The number is {:b}".format(number)) # binary
print("The number is {:x}".format(number)) # hexadecimal
print("The number is {:o}".format(number)) # octal
print("The number is {:e}".format(number)) # scientific notation
