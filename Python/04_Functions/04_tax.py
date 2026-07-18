def vat(price, rate):
    return price * (100 +rate)/100

orders = [ 100, 150, 200 ]

for price in orders:
    final_amount = vat(price, 10)
    print(f"Original: {price}, Final with vat: {final_amount}")