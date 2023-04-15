# lambda functions = function written in one line, anonymous functions, can only have one expression
# lambda parameters: expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z

full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(5, 5))
print(add(5, 5, 5))

print(full_name("John", "Doe"))
print(age_check(17))
