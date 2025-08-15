import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    
    while True:
        try:
            # Get player's guess
            guess = int(input("\nEnter your guess (1-100): "))
            attempts += 1
            
            # Check if guess is valid
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            # Check if guess is correct
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"You took {attempts} attempts to win!")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
        except ValueError:
            print("Please enter a valid number!")
            continue

if __name__ == "__main__":
    # Start the game
    number_guessing_game()
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            print("\n" + "="*50 + "\n")
            number_guessing_game()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'.")
