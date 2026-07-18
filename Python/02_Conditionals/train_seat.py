train_seat = input(f"Enter the type of seat you wish to have (Sleeper/AC/General) :").lower()

match train_seat:
    case "sleeper":
        print(f"Sleeper - No AC, Beds avialable")
    case "AC":
        print(f"Ac - Air Conditioned,  Comfy ride")
    case "general":
        print(f"General - Cheapest, No reservation")
    case _ :
        print(f"Invalid seat type")