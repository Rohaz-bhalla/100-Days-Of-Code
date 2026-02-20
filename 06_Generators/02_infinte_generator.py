def bubu_maker():
    count = 1
    while True:
        yield f"Added another bubu {count}"
        count += 1

dudu = bubu_maker()
dudu2 = bubu_maker()

for _ in range(5):
    print(next(dudu))

for _ in range(6):
    print(next(dudu2))