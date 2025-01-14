from art import logo, vs
from game_data import data
import random
import os

# Set inital variables
length = len(data)
print(logo)
gameOver = False
currentScore = 0

while not gameOver:
    # Choose random 
    firstOption = random.randint(0, length - 1)
    secondOption = random.randint(0, length - 1)
    while firstOption == secondOption:
        secondOption = random.randint(0, length - 1)
    print(f"Compare A: {data[firstOption]["name"]}, a {data[firstOption]["description"]} from {data[firstOption]["country"]}")
    print(vs)
    print(f"Compare B: {data[secondOption]["name"]}, a {data[secondOption]["description"]} from {data[secondOption]["country"]}")
    # Determine most followed option
    winner = ""
    if data[firstOption]["follower_count"] > data[secondOption]["follower_count"]:
        winner = "a"
    else:
        winner = "b"
    playerChoice = input("Who do you think has more followes? Type 'A' or 'B': ").lower()
    # Clear console and check if player chose right
    os.system('clear')
    print(logo)
    print(f"{data[firstOption]["name"]} has {data[firstOption]["follower_count"]} millioin followers while {data[secondOption]["name"]} has {data[secondOption]["follower_count"]} million followers.")
    if winner == playerChoice:
        currentScore+=1
        print(f"You're right! Current Score: {currentScore}")
    else:
        print(f"Sorry that's wrong... Final Score: {currentScore}")
        currentScore = 0
        gameOver = True

    
    