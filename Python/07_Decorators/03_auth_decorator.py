from functools import wraps

def auth_status(func):
    @wraps(func)
    def wrapper(user_role,  *args, **kwargs):
        if user_role != "admin":
            print("Access denied, admins only")
        # elif user_role == "user":
        #     print("Normal users are not allowed to access admin panel...!")
            return None
        else:
            return func( user_role, *args,**kwargs )
    return wrapper

@auth_status
def access_passwords(role, secure = "no"):
    print(f"Access granted for {role}, your password secure status is => {secure}")

access_passwords("user", secure="no")
access_passwords("admin", secure="yes")