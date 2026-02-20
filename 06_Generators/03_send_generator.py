def send_files():
    print("Welcome...! Send us your files...")
    order = yield
    while True:
        print(f"Processing your files => {order}")
        order = yield

x = send_files()
next(x)

x.send("Python")
x.send("Java")
x.send("Ruby on rails")
x.send("C++")