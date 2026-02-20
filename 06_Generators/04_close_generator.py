def func1():
    yield "Chocolate"
    yield "Toffee"

def func2():
    yield "Chai"
    yield "Coffee"

def comb_func():
    yield from func1()
    yield from func2()

for x in comb_func():
    print(x)

def try_func():
    try:
        while True:
            order = yield "waiting for orders"
            print(f"order is => {order}")

    except:
        print("Now we are closed")

    finally:
        print("This will always run")

y = try_func()
print(next(y))

y.send("came from bottom")

y.close()