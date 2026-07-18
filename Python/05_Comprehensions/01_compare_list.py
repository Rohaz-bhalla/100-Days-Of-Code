any_list = [
    "Chocolate cake",
    "Pineapple cake",
    "Cheese cake"
]

any_loop = [ my_cake for my_cake in any_list if not "Cheese cake" in my_cake ]
print(any_loop)

# they follow
# [expression for item in iterable if condition]
# stores everything onto RAM