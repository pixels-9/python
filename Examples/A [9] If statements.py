# if statement = a block of code that will execute if it's condition is true
# elif statement = a block of code that will execute if the previous if statement is false and it's condition is true
# else statement = a block of code that will execute if all the previous if and elif statements are false

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")