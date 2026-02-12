# validate user input exercise
 #1 username is no more than 12 characters
 #2 username must not contain spaces
 #3 username must not contain digits

username = input("Enter username : ")

if len(username) > 12:
    print("Username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username can't be contain any space")
elif not username.isalpha() :
    print("Username can't be contain any digis")
else:
    print(f"Hello {username}")