from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

p1 = Product(id=1, name="Laptop", price=999.99, in_stock=True)
p2= Product(id=2, name="Laptop", price=278.99,)
# Product1 = Product( name="Laptop")

# 3. FIX: Converting p2 to a dictionary so we can unpack it into a new object
# This is how you "copy" data from one model to another
prod_data = p2.model_dump() 
prod_clone = Product(**prod_data)

print(f"Original P2: {p2}")
print(f"Cloned Prod: {prod_clone}")