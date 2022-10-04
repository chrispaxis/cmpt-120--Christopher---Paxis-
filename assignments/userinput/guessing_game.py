def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''
    print("Lets play a guessing game. You will have 3 attempts. If you give up type 'quit'.")
    
    answer = "crab"
    guess = None
    guess_count = 0
    guess_limit = 3
    
    while guess != answer:
        guess = input ("Guess an animal: ").lower()
        guess_count += 1
        if guess == answer:
            print("Wow, you guessed correct!")
            break
        elif guess_count == guess_limit:
            print("Out of guesses!")
            break
        elif guess == "quit":
            print("Exiting...")
            break
        else: 
            print("Thats not right, try again!")

        
    return None 

start()