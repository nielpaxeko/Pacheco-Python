from turtle import Turtle, Screen
import random

race_is_on = False
canvas = Screen()
canvas.setup(width=500, height=400)
user_bet = canvas.textinput(title="Make your Bet!", prompt="Which turtle will win the race? (Enter a color): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x_coord = -230
y_coord = -70
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x_coord, y_coord)
    turtles.append(new_turtle)
    y_coord+=30

if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            race_is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You guessed correctly!!! the {winner} turtle has won")
            else:
                print(f"You guess was wrong... the {winner} turtle has won")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


canvas.exitonclick