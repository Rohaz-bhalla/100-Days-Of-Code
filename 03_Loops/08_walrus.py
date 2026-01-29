# value = 5

# if (remainder := value % 5) == 0:
#     print(f"remainder is {remainder}")

flavours = ["masala", "ginger", "rose"]

print(f"Avialable flavours are : {flavours}")

while(flavour := input("Choose your avialable flavours: ") ) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"you choose {flavour} chai")