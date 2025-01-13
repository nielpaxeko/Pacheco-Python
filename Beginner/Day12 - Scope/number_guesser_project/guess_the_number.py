from art import logo
import random

def chooseDifficulty():
    """Returns the number of attempts the user will be given at the start of the game based on the chosen difficulty."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Please enter a valid difficulty!")
        return chooseDifficulty()

def game(remainingGuesses):
    """Make player guess until they succeed or run out of guesses"""
    while remainingGuesses > 0:
        print(f"You have {remainingGuesses} remaining to guess the number. ")
        playerGuess = int(input("Make a guess: "))
        # IF player guesses correctly
        if playerGuess == randomNumber:
            print(f"You guesses correctly! The number was {randomNumber}!")
            print(f"You had {remainingGuesses} guesses left. ")
            print("GAME OVER")
            break
        # IF higher guess
        elif playerGuess > randomNumber:
            print("Too high.")
            remainingGuesses -= 1
        # IF lower guess
        elif playerGuess < randomNumber:
            print("Too low.")
            remainingGuesses -= 1
        # IF player is a is absolute dogwater at the game and can't understand basic instructions
        else:
            print("Please type a valid guess")
        # IF player runs out of guesses
        if remainingGuesses == 0:
            print(f"You ran out of guesses, the number was {randomNumber}")
            print("GAME OVER")
            
# Start Game
print(logo)
print("Welcome to the number guessing game!!!")
print("I am thinking of a number between 1 and 100. ")
randomNumber = random.randint(1, 100)
# Choose Difficulty
remainingGuesses = chooseDifficulty()
game(remainingGuesses)