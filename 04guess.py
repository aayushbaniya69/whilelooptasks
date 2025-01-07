i = True
password = "open sesame"

while i:
    pas = input("Guess the password : ")
    if pas == password:
        print("Access granted!")
        break
    else:
        print("Wrong password, try again.")
        continue
    

