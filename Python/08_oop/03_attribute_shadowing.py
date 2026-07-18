class coffee:
    Taste = "Excellent"
    Rating = "⭐⭐⭐⭐"

cup = coffee()
print(f"The taste of Coffee is: {coffee.Taste}")
print(f"The Rating of Coffee is: {coffee.Rating}")

cup.Taste = "Good"
cup.color = "black"
print(f"After changing taste: {cup.Taste}")
print("Color of cup is:", cup.color)
print(f"Direct class taste: {coffee.Taste}")

del cup.Taste
del cup.color
print(cup.Taste)

#This has no direct linkage with top class
# print(cup.color) 