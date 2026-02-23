import random

# Generate secret number
secret = random.randint(1, 100)

# Attempt counter
attempts = 0

print("🎯 I'm thinking of a number between 1 and 100...")

while True:
    # Get user input
    guess = input("Your guess: ")
    guess = int(guess)
    attempts += 1

    # Compare guess with secret number
    if guess > secret:
        print("⬆️ Too high!")
    elif guess < secret:
        print("⬇️ Too low!")
    else:
        print(f"✅ Correct! You got it in {attempts} attempts!")

        play_again = input("Play again? (y/n): ")

        if play_again == "y":
            secret = random.randint(1, 100)   # reset number
            attempts = 0
            print("\n🎮 New game started!\n")
        else:
            print("Thanks for playing! 👋")
            break
