email = input("Enter your email  : - ")

index = email.index("@")        #gives index value of @

username = email[:index]        #gives before @ value

# domain = email[index:]          #gives after @ value


# and if you want to exclude @ then use index+1 for grabbing the @ value

domain = email[index + 1 :]

print(f"your username is {username} and your domain is {domain}")