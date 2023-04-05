# loop control statements: Break, Continue, Pass

# break: Terminates the loop
# continue: Skips the current iteration of the loop
# pass: Does nothing

while True:
    name = input("What is your name? ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)