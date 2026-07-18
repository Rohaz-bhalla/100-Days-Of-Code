class cake_eater:
    pass

class cake_lover:
    pass

print(type(cake_eater))

cheesecake = cake_eater()

print(type(cheesecake))
print(type(cheesecake) is cake_eater)
print(type(cheesecake) is cake_lover)