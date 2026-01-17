import math

# The formula for the circumference (C) of a circle is either C = πd (pi times the diameter) or C = 2πr (2 times pi times the radius)

radius = float(input("Enter the radius of a circle : "))

circumference = 2 * math.pi * radius

print(f"The circumference is {round(circumference, 2)}")