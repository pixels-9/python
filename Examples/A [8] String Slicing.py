# slicing = create a substring by extracting elements from another string via indexing[start:stop:step] or slice()

name = "John Doe"

firstName = name[:4]       # [0:3]
lastName = name[5:]        # [4:end]
funkyName = name[::2]      # [0:end:2]
reversedName = name[::-1]  # [0:end:-1]

print(name)
print(firstName)
print(lastName)
print(funkyName)
print(reversedName)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
