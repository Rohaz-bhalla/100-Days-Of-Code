def serve_top():
    serve_type = "Blueberry" #Local scope
    print(f"Serving the cake in local scope: {serve_type}")


cake_type = "Chocolate"
serve_top()
print(f"Outside Function: {cake_type}")


def cake_counter():
    cake_order = "velvet" #Enclosing scope i.e Nested

    def print_order():
        cake_order = "cheesecake" #Inner scope
        print("Inner scope :", cake_order)
        
    print_order()
    print("outer scope", cake_order)

cake_order = "pineapple" #Global scope variable at zero indentation
cake_counter()
print("Global :", cake_order)