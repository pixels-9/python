# dictionary comprehension = a way to create a new dictionary with less syntax + can mimic lambda functions, easier to read

# dictionary = {key: value for (key, value) in iterable}
# dictionary = {key: value for (key, value) in iterable if condition}
# dictionary = {key: value (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

# ---------------------------------------------------------------------------------------------------------------------------------------------------
citiesInFahrenheit = {"New York": 32,
                        "Boston": 75,
                        "Miami": 90,
                        "Los Angeles": 100,
                        "Chicago": 50}
citiesInCelcius = {key: round((value-32) * (5/9)) for (key, value) in citiesInFahrenheit.items()}
print(citiesInCelcius)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
weather = {"New York": "Snowing",
           "Boston": "Sunny",
           "Miami": "Sunny",
           "Los Angeles": "Raining",
           "Chicago": "Cloudy"}
sunny_weather = {key: "It is sunny here!" for (key, value) in weather.items() if value == "Sunny"}
print(sunny_weather)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
cities = {"New York": 32,
            "Boston": 75,
            "Miami": 90,
            "Los Angeles": 100,
            "Chicago": 50}
descCityTemps = {key: "Warm" if value >= 40 else "Cold" for (key, value) in cities.items()}
print(descCityTemps)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def check_temp(value):
    if value >= 40:
        return "Warm"
    else:
        return "Cold"
cities = {"New York": 32,
            "Boston": 75,
            "Miami": 90,
            "Los Angeles": 100,
            "Chicago": 50}
descCityTemps = {key: check_temp(value) for (key, value) in cities.items()}
print(descCityTemps)