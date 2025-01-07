import random

random_number = random.randint(1,10)
print(random_number)
i = 0
while True:   
    num = int(input("Guess the number : "))
    if num == random_number:
        print("Correct")
        print(f"number of attempts : {i}")
        break
    else:
        if num < random_number:
            print("Guess higher")
        else:
            print("Guess lower")
    i = i + 1


