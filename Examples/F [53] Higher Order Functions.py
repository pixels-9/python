# higher order functions = functions that eather take other functions as arguments or return functions as results

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): # hof takes a function as an argument
    text = func("Hello World!")
    print(text)

hello(loud)
hello(quiet)

def denominator(x):
    def numerator(y):
        return y / x
    return numerator

divide = denominator(2)
print(divide(4)) # divide 4 by 2
