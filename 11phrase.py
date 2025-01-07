count = 0


while count < 4:
    word = input("Enter the word : ").lower()
    if word == "good luck":
        count += 1
        pass
        if count == 2:
            print(f"You typed the same word {count} times.")
        elif count == 3:
            print(f"You typed good luck {count} times.")
            break
    else:
        print("You entered wrong message. Please type 'good luck' ")
     
    
