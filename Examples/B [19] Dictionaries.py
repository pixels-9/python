# dictionary = A mutable data type that stores mappings of unique keys to values, fast lookup

capitals = {"USA": "Las Vegas",
            "France": "Paris",
            "Germany": "Berlin"}

capitals.update({"USA": "Washington D.C."})
capitals.update({"Russia": "Moscow"})

# capitals.pop("USA")
# capitals.clear()

print(capitals.get("USA"))
print(capitals.get("Russia"))
print(capitals.get("China", "Not Found"))

print(capitals.keys())
print(capitals.values())
print(capitals.items())
