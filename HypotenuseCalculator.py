import math

a = float(input("Enter A side : "))
b = float(input("Enter B side : "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"C side is : {round(c,2)}")