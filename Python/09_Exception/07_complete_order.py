class AnyException(Exception):
    pass

def bill(flavour, cups):
    menu = { "Ginger" : 20, "Pudina" : 40 }
    try:
        if flavour not in menu:
            raise AnyException("Not Available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai is {total}")

    except Exception as e:
        print("Error: ", e)
    finally:
        print("Rolling to next order... --->")

bill("mint", 2)
bill("masala", "three")
bill("Ginger", 3)