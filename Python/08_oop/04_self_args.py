class coffee:
    price = "60"

# Function belongs to class and used self is called a Method, always check for indentation 
    def coffee_price(self):
        return f"A {self.price}ml cup"

shop = coffee()
print(shop.coffee_price())
print(coffee.coffee_price(shop))

shop_two = coffee()
shop_two.price = 100
print(coffee.coffee_price(shop_two))