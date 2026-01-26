isBoiling = True
stri_count = 5
total_actions = stri_count + isBoiling 
#upcastinig, isBoiling got upcast as 1, as bool is subclass of int, its dangerous

print(f"total : {total_actions}") 

milk = 0
print(f"is milk present {bool(milk)}") 
#0 got treated as false value

water_hot = True
milk_hot = True

print(f"can serve? {water_hot + milk_hot}")
# + operator made them add => 2

serve = water_hot and milk_hot
print(f"using and operator to serve : {serve}")