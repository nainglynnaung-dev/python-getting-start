attempt=0
max_attempt=3
authenticate=False

while attempt < max_attempt:
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if username=="admin" and password=="password":
        authenticate=True
        break


    else:
        print("Invalid username or password")
        attempt=attempt+1

if authenticate==True:
    print("Login successful")
else:
    print("Login failed")