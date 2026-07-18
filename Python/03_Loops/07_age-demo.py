names = [("Rohaz", 21), ("Hitaishi", 22), ("Ram", 17)]

for idx, age in names:
    if age >= 18:
        print(f"{idx} is eligible for tickets")
    else:
        print(f"{idx} is not eligble for tickets")