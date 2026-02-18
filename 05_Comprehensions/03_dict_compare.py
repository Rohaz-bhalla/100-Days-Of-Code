coffee_prices_inr = {
    "Black Coffee" : 50,
    "Latte Coffee" : 80,
    "Milk Coffee"  : 40
}

coffee_prices_usd = { coffee : price / 80 for coffee, price in coffee_prices_inr.items() }
print(coffee_prices_usd)

# just like lists, but you use curly braces {} and define a key: value pair.
# used for mapping {'a' : 1}