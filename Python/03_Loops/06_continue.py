stocks = ["out of stock", "zomato", "swiggy", "discontinued"]

for idx in stocks:
    if stocks == "out of stock":
        continue
    if stocks == "discontinued":
        print(f"The stocks are {idx}")
        break
    print(f"{idx} item found")