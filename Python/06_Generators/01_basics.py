def serve_cake():
    yield "Cake 1: Cheese Cake"
    yield "Cake 2: Chocolate Cake"
    yield "Cake 3: Blueberry Cake"

shop = serve_cake()

# for x in shop:
#     print(x)

#A Generator is a special type of function in Python that allows you to iterate over a sequence of values without storing them all in memory at once. it runs each line one by one
print(next(shop))
print(next(shop))