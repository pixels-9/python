# map() = applies a function to all the items in a list
# map(function, list)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

usdToEur = lambda usd: (usd[0], usd[1] * 0.90) # USD TO EUR rate as of 16th of April 2023
storeEur = list(map(usdToEur, store))

eurToUsd = lambda eur: (eur[0], eur[1] / 0.90) # USD TO EUR rate as of 16th of April 2023
storeUsd = list(map(eurToUsd, store))

price = lambda item: item[1]

for item in sorted(storeEur, key=price):
    print(item[0], end=" ")
    print(item[1])

for item in sorted(storeUsd, key=price):
    print(item[0], end=" ")
    print(item[1])
