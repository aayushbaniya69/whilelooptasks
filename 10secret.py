secret_word = "python"
i = True

while i:
    
        guess = input("Enter the guess word : ").lower()
        if guess == secret_word:
            print("Congratulations, You guessed the word!")
            
            ask = input("Do you want to exit write 'exit' ? ").lower()
            if ask == "exit":
                break
        else:
            print("Incorrect, try again")