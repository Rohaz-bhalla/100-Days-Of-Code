device_status = "active"
temperature = int(input(f"Enter the room temperature :"))

if device_status == "active":
    if temperature > 35:
        print(f"High temperature alert...!!")
    else:
        print(f"Temperature is fine...!!")