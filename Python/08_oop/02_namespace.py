class cake:
    #properties
    manufacturer = "Santos bakery"

print(cake.manufacturer)

cake.is_Tasty = True
print(cake.is_Tasty)

cheesecake = cake()
print(f"The cake was made by {cheesecake.manufacturer}")
print(f"The taste of cake is represented as a boolean value => {cheesecake.is_Tasty}")

cheesecake.is_Tasty = False
print("Taste description in main class is:", cake.is_Tasty)
print(f"Is Cheesecake tasty? => {cheesecake.is_Tasty}")

cheesecake.ingredients = [
    "Cheese", "Milk", "Biscoff"
]
print(f"The ingredients used are: {cheesecake.ingredients}")
