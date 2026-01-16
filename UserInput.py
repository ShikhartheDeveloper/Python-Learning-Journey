input("To unlock type shikharisking : ")

#Entering your name and passing input to a variable

name = input("Enter your name : ")
print(f"Hey {name}")

age = input("Enter your age : ")
print(f"You are {age} years old")


# what if i want to perform a math operation just increase the age by ones 1

# age = age + 1
# print(age)

# it gives error because the datatype of (input ) is String , It Will always return string so firstly typecast into Int

age = int(age)
age = age + 1
print(age)

#now if you enter 21 it gives you 22 because of increase by ones

# for better optimization use single line of code like

mob_no = int(input("Enter your mobile number : "))
print(f" Your mobile number is : {mob_no}" )
print(type(mob_no))