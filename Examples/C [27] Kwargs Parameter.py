# **kwargs = parameter that will pack all keyword arguments into a dictionary

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Sir.",first="John", middle="Bob", last="Doe")