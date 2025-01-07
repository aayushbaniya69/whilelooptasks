import random


i = True

while i: 
    
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print(num1)
    print(num2)
    mul = num1 * num2

    question = input("Do you want to exit : ").lower()
    if question == "exit":
        break
    else:
        print("Please enter a valid message or type 'exit' to stop.")
    
    ans = int(input("Enter answer of the multiplication : "))
    if mul == ans:
        print("Correct")      
    elif mul != ans:
        print("Incorrect, try again")
    else:
        pass
    