# assign functions to variables = the same as assigning any other value to a variable

def hello():
    print("Hello World!")

print(hello) # prints location of function in memory in hexadecimal
hi = hello
print(hi) # prints location of function in memory in hexadecimal
hi() # calls the hello function because hi is assigned to hello, like an alias
say = print
say("Hello World!") # calls the print function because say is assigned to print, like an alias
