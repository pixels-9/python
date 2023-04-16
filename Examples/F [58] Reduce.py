# reduce() = apply a function to an iterable and reduce it to a single cumulative value + performs function on first two elements and repeats process until 1
# value remains 

import functools

letters = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
