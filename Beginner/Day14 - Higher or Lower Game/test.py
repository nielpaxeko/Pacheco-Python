from art import logo, vs
from game_data import data
import random
import os

# Start Game
game_over = False
score = 0
print(logo)
while not game_over:
    # Present choices
    firstCelebrity = random.choice(data)
    secondCelebrity = random.choice(data)
    print("Compare A: " + firstCelebrity["name"] + ", a " + firstCelebrity["description"] + " from " + firstCelebrity["country"])
    print(vs)
    print("Compare B: " + secondCelebrity["name"] + ", a " + secondCelebrity["description"] + " from " + secondCelebrity["country"])
    # Select Winner
    winner = ""
    followerCountA = firstCelebrity["follower_count"]
    followerCountB = secondCelebrity["follower_count"]
    if followerCountA > followerCountB:
        winner = "a"
    else:
        winner = "b"
    # Get Player Choice and determine outcome
    playerChoice = input("Who do you think has more followers? A or B? ").lower()
    os.system("clear")
    print(logo)
    print(f"{firstCelebrity["name"]} has {followerCountA} millioin followers while {secondCelebrity["name"]} has {followerCountB} million followers.")
    if winner == playerChoice:
        score+=1
        print(f"That is correct. Current Score = {score}")
    else:

        print(f"Sorry that's wrong... Final Score: {score}")
        print("GAME OVER")
        game_over = True