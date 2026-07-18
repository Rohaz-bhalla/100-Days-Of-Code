class cake_order:
    def __init__(self, type_, flavour):  #constructor
        self.type = type_
        self.flavour = flavour

    def summary(self):
        return f"Your {self.type} of {self.flavour} flavour is ready...!"

order = cake_order("Cheesecake", "dry" )
print(order.summary())

order_two = cake_order("Pasta", "White sauce")
print(order_two.summary())