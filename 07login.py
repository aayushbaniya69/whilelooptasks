attempts = 4
i = 0

while i < attempts:
    if i == 3:
        print("Too many failed attempts.")
        break

    user_Name = input("Enter the username : ")
    password = input("Enter the password : ")
    if user_Name == "admin" and password == "1234":
        print("Login successful")
        break
    elif user_Name != "admin" or password != "1234":
        print("Invalid credentials, try again.")
    i = i + 1
