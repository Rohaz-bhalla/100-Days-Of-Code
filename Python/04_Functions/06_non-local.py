cake_name = "cheesecake"
def update_name():
    cake_name = "Chocolate"

    def kitchen():
        nonlocal cake_name
        cake_name = "blueberry"
        
    kitchen()
print("After kitchen update", cake_name)

update_name()