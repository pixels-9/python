# *args = parameter that will pack all arguments into a tuple

def add(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)