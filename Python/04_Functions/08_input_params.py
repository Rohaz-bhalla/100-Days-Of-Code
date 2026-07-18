cake = [1,2,3]

def edit_cake(plate):
    plate[1] = 33

edit_cake(cake)
print(cake)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # Positional Python matches the values to the variables based on the order they appear.
make_chai(tea="Green", sugar="Medium", milk="No") # Keywords we can change the order

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardamom", sweetener="honey", foam="yes")




def chai_order(order = None):
    if order is None:
        order = []
        print(order)

chai_order()