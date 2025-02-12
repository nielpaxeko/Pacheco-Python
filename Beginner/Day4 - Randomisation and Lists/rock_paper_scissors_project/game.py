import random

# I did not make this art
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Intro
print("Welcome to the rock paper scissors game!")
game_images = [rock, paper, scissors] 
# Get Player Choice
playerChoice = int(
    input("What do you choose? (Type 0 for Rock, 1 for Paper or 2 for Scissors) ")
)
# Display Player Choice
print("You have chosen:")
print(game_images[playerChoice])

# Choose and Display Random CPU choice, 
computerChoice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computerChoice])

# Choose winner based on answers
if playerChoice >= 3 or playerChoice < 0:
    print("You typed an invalid number, you lose!")
elif playerChoice == 0 and computerChoice == 2:
    print("You win!")
elif computerChoice == 0 and playerChoice == 2:
    print("You lose")
elif computerChoice > playerChoice:
    print("You lose")
elif playerChoice > computerChoice:
    print("You win!")
elif computerChoice == playerChoice:
    print("It's a draw")
