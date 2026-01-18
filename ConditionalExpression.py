# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                                             Print or assign one of two values based on a condition
#                                             X if condition else Y


num = 5
print("Positive " if num > 0 else "Negative")

# even-odd

val = 7
res = "Even" if val % 2 == 0 else "Odd"
print(res)

a=5
b=7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)




age = 17

status = "Adult " if age >= 18 else "Children"
print(status)
