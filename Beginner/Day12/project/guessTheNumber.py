from art import logo
import random

def chooseDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Please enter a valid difficulty!")
        return chooseDifficulty()

print(logo)
print("Welcome to the number guessing game!!!")
print("I am thinking of a number between 1 and 100. ")
remainingGuesses = chooseDifficulty()
randomNumber = random.randint(1, 100)
while remainingGuesses > 0:
    print(f"You have {remainingGuesses} remaining to guess the number. ")
    playerGuess = int(input("Make a guess: "))
    if playerGuess == randomNumber:
        print(f"You guesses correctly! The number was {randomNumber}!")
        print(f"You had {remainingGuesses} guesses left. ")
        break
    elif playerGuess > randomNumber:
        print("Too high.")
        remainingGuesses -= 1
    elif playerGuess < randomNumber:
        print("Too low.")
        remainingGuesses -= 1
    else:
        print("Please type a valid guess")
    if remainingGuesses == 0:
        print(f"You ran out of guesses, the number was {randomNumber}")
        print("Game Over")
