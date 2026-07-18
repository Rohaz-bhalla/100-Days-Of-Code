def OutOfIngredients_Error(Exception):
    pass

def make_coffee( milk, coffee_beans ):
    if milk == 0 or coffee_beans == 0:
        raise OutOfIngredients_Error("Missing milk or coffee beans")
    print("coffee is ready")

make_coffee(0, 1)