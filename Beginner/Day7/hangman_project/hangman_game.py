import random
from hangmanWords import word_list

logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
print(logo)
print(stages[0])
chosenWord = random.choice(word_list)
length = len(chosenWord)
display = []
for letter in range(0, length):
    display.append("_")
livesRemaining = 6
gameOver = False
guessedLetters = []
while not gameOver:
    guess = input("Guess a letter: ")
    if guess not in chosenWord and guess not in guessedLetters:
        livesRemaining -= 1
        print(f"The letter {guess} is not in the word.")
        print(f"Lives remaining = {livesRemaining}")
        guessedLetters.append(guess)
    elif guess in guessedLetters:
        print(f"You have already chose the letter {guess}, no lives will be subtracted.")
        print(f"Lives remaining = {livesRemaining}")
    else:
        guessedLetters.append(guess)
        for idx in range(length):
            if guess == chosenWord[idx]:
                display[idx] = guess
                print("You guessed correctly")
                print(f"Lives remaining = {livesRemaining}")
    print(stages[livesRemaining])
    print(display)
    if "_" not in display:
        gameOver = True
        print("You Won!!!")
    elif livesRemaining == 0:
        gameOver = True
        print("You Lost!!!")
        print(f"The word was {chosenWord}")
