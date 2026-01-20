weight = float(input("Enter your weight : "))
unit = input("Kilogram or pounds : (K or L)? : ")

if unit == "K":
    weight = weight * 2.204
    unit = "Pounds"
    print(f"You are {round(weight,2)} {unit}")
elif unit == "L":
    weight = weight / 2.204
    unit = "Kilograms"
    print(f"You are {round(weight,2)} {unit}")
else:
    print(f"{unit} is invalid...")
