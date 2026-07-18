users = [
    {"id" : 1, "total" : 100, "coupon" : "P20"},
    {"id" : 2, "total" : 200, "coupon" : "F20"},
    {"id" : 3, "total" : 300, "coupon" : "P30"}
]

discounts = {
    "P20" : (0.20, 0),
    "P30" : (0.30, 0),
    "F20" : (0, 20)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and get discounted for {discount}")