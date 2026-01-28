cup = input("Choose your cup (small/medium/large) :").lower()

if cup == "small":
    print(f"Price is 10rs")
elif cup == "medium":
    print(f"Price is 20rs")
elif cup == "large":
    print(f"Price is 30rs")
else:
    print(f"Unknown cup size")