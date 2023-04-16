# filter() = creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Pheobe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda x:x[1] >= 18
over18Friends = filter(age, friends)
for item in over18Friends:
    print(item[0])
