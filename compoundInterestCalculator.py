rate = 0
principle = 0
time = 0

while True :
    principle = float(input("Enter principle amount:- "))
    if principle < 0:
        print(f"Princliple can't be smaller or equal to zero")
    else:
        break

while True :
    rate = float(input("Enter rate of interest:- "))
    if rate < 0:
        print(f"Rate of interest can't be smaller or equal to zero")
    else:
        break

while True :
    time = int(input("Enter time in years:- "))
    if time < 0:
        print(f"Time can't be smaller or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100 ), time)

print(f"Your total Balance after {time} year/s is ${total:.2f}")

