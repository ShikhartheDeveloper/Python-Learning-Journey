num1 = float(input("Enter 1st Number : "))
num2 = float(input("Enter 2nd Number : "))
operator = input("Enter any operator (+ - x /): ")

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "x":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("invalid operation")
