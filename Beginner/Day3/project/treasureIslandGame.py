print('''
  *******************************************************************************
            |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____ /
  *******************************************************************************
  ''')
# The chest above was not my creation
# This day's project is supposed to ask the "player" to choose between two options.
# The correct options will lead the player to victort, all others will lead to a Game Over
print("Welcome to Treasure Island!!!")
direction = input("Do you want to go left or right? (L or R) ")
if direction == "R": 
    print("You got lost in the forest! GAME OVER!!!")
elif direction == "L":
    riverCrossing = input("A river stands in front of you, will you swim or wait for a boat? (S or W) ")
    if riverCrossing == "S": 
        print("You drowned! GAME OVER!!!")
    elif riverCrossing == "W":
        print("After a while, a boat passed by and takes you to the the island.")
        door = input("You found a blue and a red door, which door will you go through? (R or B) ")
        if door == "B":
            print("The room you entered was booby trapped! GAME OVER!!!")
        elif door == "R":
            print("You found the treasure inside the room! GAME CLEARED!!!!!!")