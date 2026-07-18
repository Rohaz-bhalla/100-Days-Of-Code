def cake(flavour):
    if flavour not in ["Cheese", "Blueberry", "Oreo"]:
        raise ValueError("Unsupported cake flavour")
    print(f"Preparing your {flavour} cake")

cake("Cheese")
# cake("Chocolate")