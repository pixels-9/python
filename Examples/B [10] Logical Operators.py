# Logical operators (and, or, not) = used to check two or more conditional statements

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today, stay inside.")
else:
    print("The temperature is good today, go outside")
