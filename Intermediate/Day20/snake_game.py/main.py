from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_over = False

startin_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []

for position in startin_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake_body.append(new_segment)
    
screen.update()
    
while not game_over:
    for segment in snake_body:
        segment.forward(20)







screen.exitonclick()