Menu = { "Cake" : 100, "Coffee" : 50 }

try:
    Menu["Shake"]
except KeyError:
    print("Item not available")

print("Hey...!")