def process_order(item, quantity):
    try:
        price = { "Cheese" : 20 }[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry this order isn't available")
    except TypeError:
        print(f"Quantity must be in number")

process_order("Ginger", 2)
process_order("Cheese", "two")