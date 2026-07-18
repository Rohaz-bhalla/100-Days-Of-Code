from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper( *args, **kwargs ):
        print(f"Calling: {func.__name__}")
        result = func( *args, **kwargs )
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@logging
def cake(type, Egg = "no"):
    print(f"Making your {type} Cake egg status {Egg} ")

cake("Cheesecake", Egg="yes")