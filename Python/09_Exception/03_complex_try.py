def serve_menu(food):
    try:
        print(f"Preparing your order of {food}")
        if food == "unknown":
            raise ValueError("We dont know about it")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{food} is ready")
    finally:
        print("Next order please..!!")

serve_menu("Pizza")
serve_menu("Burger")