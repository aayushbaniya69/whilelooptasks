import random
i = True

while i:
    age = input("Enter the age : ")
    if age < 18:
        print("You are a minor")
        question = input("Do you want to stop or continue ? ")
        if question == "stop":
            break
        if question == "continue":
            continue

    elif age > 18 and age < 60:
        question = input("Do you want to stop or continue ? ")
        if question == "stop":
            break
        if question == "continue":
            continue
    elif age > 60:
        question = input("Do you want to stop or continue ? ")
        if question == "stop":
            break
        if question == "continue":
            continue
    else:
        pass
    
    

