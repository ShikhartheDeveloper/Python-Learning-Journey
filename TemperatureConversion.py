temp = float(input("Enter temperature : "))
unit = input("Is this temperature in Celsius or Fahrenheit (C/F)? : ")

if unit == "F":
    temp = round((temp - 32) * 5 / 9 ,1)
    print(f"Temperature is {temp}°c")
elif unit =="C":
    temp = round((9 * temp) /  5 + 32 ,1)
    print(f"Temperature is {temp}°f")
else:
    print(f"{unit} is invalid ......")