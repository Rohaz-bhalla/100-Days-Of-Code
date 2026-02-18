coffee_sales = [
    5,12,18,20,28
]

total_cup = sum(sale for sale in coffee_sales if sale > 18 )
print(total_cup)

# (x for x in data)	A memory-efficient iterator
# works in stream i.e iterates one by one
# used during work with infinite sequence 