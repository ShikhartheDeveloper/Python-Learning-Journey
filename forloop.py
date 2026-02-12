# num = int(input("Enter any number :- "))
# for i in range(1,11):
#     print(f"{num} X {i} = {i * num}")
# print("fuck off")


#Reversed For loop

for i in reversed(range(1,11)):
    print(i)
    break

credit_card = "1234-5678-9012-3456"

for l in credit_card:
    print(l)
    break

for x in range(1,21):
    if x == 13:
        continue
    elif x == 17:
        break
    else:
        print(x)