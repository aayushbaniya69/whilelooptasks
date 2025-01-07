i = True

while True:
    ask = input("Do you want to exit ? ").lower()
    if ask.lower() == "exit":
        break
    else:
        print("Enter a valid answer, if want to exit then write 'exit' ")
        num = int(input("Enter a number : "))
        if num <= 1:
            print("The number is not prime.")
        elif num == 2:
            print("The number is prime.")  # 2 is the only even prime number
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    print("The number is not prime.")
                    is_prime = False
                    break
            if is_prime:
                print("The number is prime.")
    