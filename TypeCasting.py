name = "Coder"
age = 29
gpa = 4.7
isEmployeed = False

#Explicit TypeCasting

name = bool(name)
print(name)         #true ,  false only if String is empty""

age = str(age)
print(type(age))    #it will become string 


isEmployeed = int(isEmployeed)
print(isEmployeed)     # it gives us 0 because 0 is False and 1 is True (we have isEmpleyeed  = False that means 0)


age = float(age)
print(age)      # 29.0



#Implicit TypeCasting  - > Python converts one datatype to another datatype to avoid data loss

x = 40
y = 4.1
x = x/y
print(x)
print(type(x))            # it gives float value but it(x) was integer

