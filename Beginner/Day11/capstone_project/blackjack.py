from art import logo
import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerCards = []
computerCards = []

# Calculates score while accounting for aces
def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

# Set initial cards to players
def startGame():
    # Create player and computer's first 2 cards
    playerCards.append(random.choice(cards))
    playerCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))
    # Create and display current scores
    displayCards()
    drawCard()

# Displays cards
def displayCards():
    print(f"Your cards: {playerCards}, current score: {calculate_score(playerCards)}")
    print(f"Computer's first card: {computerCards[0]}")

# Displays the winner
def displayFinalScores():
    playerScore = calculate_score(playerCards)
    computerScore = calculate_score(computerCards)
    print(f"Your final hand: {playerCards}, final score: {playerScore}")
    print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
    if playerScore > 21:
        print("You went over, You Lose!")
    elif computerScore > 21:
        print("Computer went over, You Won")
    elif playerScore < computerScore:
        print("Computer's score is higher, You Lose!")
    elif computerScore == playerScore:
        print("Looks like it's a draw!")
    else:
        print("Your score was higher, You Won!")

# Gives player and computer a chance to draw cards
def drawCard():
    drawAgain = input("Type 'y' to get another card, type 'n' to pass: ")
    while calculate_score(computerCards) < 17:
        computerCards.append(random.choice(cards))
        print("Computer has drawn another card!")
    if drawAgain == "y":
        playerCards.append(random.choice(cards))
        displayCards()
        if calculate_score(playerCards) < 21:
            drawCard()
        else:
            displayFinalScores()
    else:
        displayFinalScores()


continueGame = True
while continueGame:
    startGameQuery = input(
        "Would you like to play a game of blackjack? (Type 'y' or 'n') "
    )
    if startGameQuery == "n":
        print("Game Over!!!")
        continueGame = False
    else:
        playerCards = []
        computerCards = []
        startGame()
