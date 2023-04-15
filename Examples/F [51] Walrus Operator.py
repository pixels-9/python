# walrus operator (:=) = operator used to assign values to variables as part of a larger expression
# aka assignment expression

# pros: less code, more readable, less variables, less memory
# cons: not available in Python 3.7 and below

# happy = True
# print(happy)
print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like? (Type quit to exit) ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while food := input("What food do you like? (Type quit to exit) ") != "quit":
    foods.append(food)
