item = input("What item would you like to buy? : ")
price = float(input("What is the price of item? : "))
quantity = int(input("How many would you like to buy? : "))

total_price = price * quantity          #it gives data in float to avoid data loss (implicit typecasting)

print(f"You have bought {quantity} of {item}")
print(f"Your total is : ${round(total_price , 2)}")


#Extra what i learn today is

# “round() makes numbers behave like humans, not machines.”

# round(4.6)     # 5
# round(4.4)     # 4
# round(3.14159, 2)  # 3.14