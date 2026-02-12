# food  = input("Enter any Food you like (q to quit):- ")

# while not food == "q":
#     print(f" You like {food}")
#     food  = input("Enter another Food you like (q to quit)")
# print("Bye...")


num = int(input("Enter any number between 1 - 10"))

while num < 1 or num > 10:
    print(f"{num} is not valid...")
    num = int(input("Enter any number between 1 - 10"))

print(f"you chose {num}")