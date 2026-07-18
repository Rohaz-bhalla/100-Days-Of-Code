coffees = [
    "Black coffee",
    "Vietnamese coffee",
    "Normal coffee"
]

unique_coffee = {milk for milk in coffees}
print(coffees)

recipes = {
    "Black coffee": ["Water", "Coffee"],
    "Vietnamese": ["Syrup", "Coffee", "Milk"],
    "Normal coffee": ["Milk", "Coffee"]
}

unique_recipes = { powder for ingredients in recipes.values() for powder in ingredients }
print(unique_recipes)

# removes duplicates
# {x for x in data}