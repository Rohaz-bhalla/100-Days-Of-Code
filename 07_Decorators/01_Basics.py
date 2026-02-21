from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("The Function Before the wrapper")
        func()
        print("The Function After the wrapper")
    return wrapper

@my_decorator
def greet():
    print("Hello from Decorator class in python")

greet()
print(greet.__name__)