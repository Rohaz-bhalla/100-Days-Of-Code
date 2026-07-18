class cake_maker:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        return f"Preparing {self.type} cake..."

class cake_ingredients:
    # We add __init__ here so it can accept the "type" from the shop
    def __init__(self, type_):
        self.type = type_

    def ingredients(self):
        print(f"Adding Milk, Biscoff, Vanila for the {self.type} base...")

class cake_shop:
    cook_cls = cake_maker

    def __init__(self):
        # This line passes "Chocolate" to whatever class is in cook_cls
        self.cook = self.cook_cls("Chocolate")
    
    def serve(self):
        print(f"Serving your {self.cook.type} in cake saloon")

# We inherit from cake_shop to get the __init__ and serve methods
class fancyCakeShop(cake_shop):
    cook_cls = cake_ingredients

# Testing the code
shop = cake_shop()
fancy = fancyCakeShop()

shop.serve()
fancy.serve()
fancy.cook.ingredients()