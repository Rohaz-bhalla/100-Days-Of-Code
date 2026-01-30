cake_type = "cheesecake"

def front_table():
    def kitchen():
        global cake_type
        cake_type = "chocolate"
    kitchen()

print("Final global element is :", cake_type)