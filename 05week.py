i = True

while i:
    week = input("Enter a day of the week : ").lower()
    if week == "sunday":
        print("Enjoy your weekend!")
        break
    else:
        print("It's not the weekend yet.")
        continue
        
