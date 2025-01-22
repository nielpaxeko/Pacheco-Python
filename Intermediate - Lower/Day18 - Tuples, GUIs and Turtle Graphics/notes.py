# Day 18 - Turtle Graphics
from turtle import Turtle, Screen
import random as r

screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.speed(0)
screen.colormode(255)

def change_colour():
    tim.color(r.randint(0,255), r.randint(0,255), r.randint(0,255))

# Turtle Challenge 1 - Draw Square

# for i in range (4):
#     tim.forward(100)
#     tim.right(90)

# Turtle Challenge 2 - Dashed Line

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
    
# Turtle Challenge 3 - Dashed Line

def draw_shapes():
    for i in range(3,11):
        angle = 360 / i
        change_colour()
        for _ in range (i):
            tim.forward(100)
            tim.right(angle)
# draw_shapes()

# Turtle Challenge 4 - Random Walk
def changeDirection():
    direction = r.randint(1,4) * 90
    tim.right(direction)
    
# for i in range(100):
#     change_colour()
#     changeDirection()
#     tim.forward(15)

# Turtle Challenge 5 - Spirograph

def spirograph(gap):
    for i in range(int(360/gap)):
        change_colour()
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

spirograph(10)

screen.exitonclick()