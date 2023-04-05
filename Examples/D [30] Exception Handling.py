# exception = events detected during execution that interrupt the normal flow of a program

# try: block of code to be attempted (may lead to an exception)
# except: block of code will execute in case there is an exception in try block
# else: block of code will execute if there is no exception in try block
# finally: a final block of code to be executed, regardless of an exception

try:
    x = int(input("Enter a numerator: "))
    y = int(input("Enter a denominator: "))
    print(x/y)
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero!")
except ValueError as e:
    print(e)
    print("You must enter a whole number!")
